d_users = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
    }
def authorization(users):
    while True:
        login = input('Введите логин:\n(выход - exit)\n')
        if login == 'exit':
            return False

        if login in users:
            password = input('Введите пароль:\n')
            if password == users.get(login):
                return True
            else:
                print('неверный пароль')
                continue
        else:
            print('неверный логин')
            continue
    #print(d.get('user1'))
