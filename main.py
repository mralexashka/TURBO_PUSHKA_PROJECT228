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


while True:
    print('"1" - вход в калькулятор \n"2" - проверка на полиндром \n"exit" - выход из программы')
    s = input()
    if s == 'exit': #выход из приложения
        break
    elif s == '1': #вход в калькулятор
        calculator()
    elif s == '2':
        is_palindrome() #в проверку на палиндром
    else:
        print('Неверная команда PES')


