import psycopg2


def is_palindrome():
    while True:
        string = input('"back" - назад.\nВведите слово/число:\n')
        if string == 'back':
            break
        flag = True
        if string != string[::-1]:
            flag = False
        print(flag)#


def calculator():
    while True:
        op = input('"back" - назад.\n Введите операцию ("+" "-" "*" "/")\n')
        if op == 'back':
            break
        elif op not in '+-*/':
            print('Неверный ввод операции')
            continue
        a = input('Введите первое число\n')
        if not a.isdigit():
            print('Это не число')
            continue
        b = input('Введите второое число\n')
        if not b.isdigit():
            print('Это не число')
            continue
        a = float(a)
        b = float(b)
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            if b == 0:
                print('Ты что, фронттендер?')
            else:
                print(a / b)


def authorization(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    logins = [user[1] for user in users]
    while True:
        login = input('Введите логин:\n("back - назад")\n')
        if login == 'back':
            return 0

        if login in logins:
            password = input('Введите пароль:\n')
            for user in users:
                if login in user and password in user:
                    cursor.close()
                    return user
            else:
                print('неверный пароль')
                continue
        else:
            print('неверный логин')
            continue


def registration(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    logins = [user[1] for user in users]

    while True:

        new_login = input('Придумайте логин: \n"back" - назад\n')
        if new_login == 'back':
            return ''
        elif new_login in logins:
            print('Такой логин уже занят')
            continue
        elif new_login == 'exit':
            print('Такой логин недопустим')
            continue
        else:
            new_password = input('Придумайте пароль (от 8 символов):\n')
            if len(new_password) < 8:
                print('Недопустимый пароль')
                continue
            else:
                second_password = input('Повторите пароль\n')
                if second_password != new_password:
                    print('Пароли не совпадают')
                    continue
                else:
                    cursor.execute(f"INSERT INTO users (login, password) VALUES ('{new_login}', '{new_password}')")
                    connection.commit()
                    cursor.close()
                    return new_login


def notes(user_id, connection):
    cursor = connection.cursor()
    while True:
        cursor.execute(f"SELECT * FROM notes WHERE id={user_id}")
        all_notes = cursor.fetchall()
        s = input('"1" - Вывести заметки \n"2" - Добавить заметку \n"3" - Удалить заметку \n"back" - Назад\n')
        if s == '1':
            i = 1
            print(all_notes)
            for user_note in all_notes:
                if user_note[0] == user_id:
                    print(str(i)+') '+user_note[1])
                    i += 1
        elif s == '2':
            text = input('Введите текст новой заметки\n')
            cursor.execute(f"INSERT INTO notes (id, note) VALUES ({user_id}, '{text}')")
            connection.commit()
        elif s == '3':
            n = input('Введите номер заметки для удаления\n')
            if not n.isdigit():
                print('Это не число')
                continue
            else:
                n = int(n)
                if n > len(all_notes):
                    print('Номер больше, чем кол-во заметок')
                    continue
                else:

                    cursor.execute(f"DELETE FROM notes WHERE note='{all_notes[n-1][1]}'")
                    connection.commit()
                    continue
        elif s == 'back':
            cursor.close()
            break
        else:
            print('Неверная команда')
            continue


while True:
    conn = psycopg2.connect(dbname="turbo_puska_db", user="postgres", password="alexashka", host="127.0.0.1",
                            port="5432")
    s = input('"1" - авторизация \n"2" - регистрация\n"exit" - выход из программы\n')
    if s == "exit": #выход из приложения
        conn.close()
        break
    elif s == '2':  #регистрация
        new_login = registration(conn)
        if new_login != '':
            print(f'Вы зарегестрировались, {new_login}!\n')
            continue

    elif s == '1':  #авторизация
        user = authorization(conn)
        if user != 0:
            s = input(f'Привет, {user[1]}! \n"1" - вход в калькулятор \n"2" - проверка на полиндром \n'
                      f'"3" - меню заметок \n"back" - назад\n')
        else:
            continue
        if s == 'back':
            continue
        elif s == '1': #вход в калькулятор
            calculator()
        elif s == '2':  #в проверку на палиндром
            is_palindrome()
        elif s == '3':  #заметки
            notes(user[0], conn)
        else:
            print('Неверная команда')


