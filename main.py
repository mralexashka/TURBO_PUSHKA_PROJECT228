class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.notes = []


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


def authorization(users):
    while True:
        login = input('Введите логин:\n("back - назад")\n')
        if login == 'back':
            return ''

        if login in users:
            password = input('Введите пароль:\n')
            if password == users.get(login):
                for u in users_list:
                    if u.login == login:
                        return u
            else:
                print('неверный пароль')
                continue
        else:
            print('неверный логин')
            continue


def registration(users):
    while True:
        new_login = input('Придумайте логин: \n"back" - назад\n')
        if new_login == 'back':
            return 0
        elif new_login in users:
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
                    new_user = User(new_login, new_password)
                    return new_user


def notes(user):
    while True:
        s = input('"1" - Вывести заметки \n"2" - Добавить заметку \n"3" - Удалить заметку \n"back" - Назад\n')
        if s == '1':
            for note in user.notes:
                print(str(user.notes.index(note)+1)+') '+note)
        elif s == '2':
            user.notes.append(input('Введите текст новой заметки\n'))
        elif s == '3':
            n = input('Введите номер заметки для удаления\n')
            if not n.isdigit():
                print('Это не число')
                continue
            else:
                n = int(n)
                if n > len(user.notes):
                    print('Номер больше, чем кол-во заметок')
                    continue
                else:
                    del user.notes[n-1]
                    continue
        elif s == 'back':
            break
        else:
            print('Неверная команда')
            continue


user1 = User('user1', 'password1')     #парочка пользователей
user2 = User('user2', 'password2')
users_keys = {
    user1.login: user1.password,
    user2.login: user2.password
}
users_list = [user1, user2]
user1.notes = ['Позвонить Кирюхе', '1.10 - забронить дом', 'номер хаты 67']


while True:
    s = input('"1" - авторизация \n"2" - регистрация\n"exit" - выход из программы\n')
    if s == "exit": #выход из приложения
        break
    elif s == '2':  #регистрация
        user = registration(users_keys)
        if user != 0:
            print(f'Вы зарегестрировались, {user.login}!\n')
            users_keys[user.login] = user.password
            continue

    elif s == '1':  #авторизация
        user = authorization(users_keys)
        if user != '':
            s = input(f'Привет, {user.login}! \n"1" - вход в калькулятор \n"2" - проверка на полиндром \n'
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
            notes(user)
        else:
            print('Неверная команда')


