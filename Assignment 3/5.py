username = 'python'
password = 'rules'
x = 0

while True:
    username_input = str(input('Enter username: '))
    password_input = str(input('Enter password: '))
    if x == 5:
        print('Acces denied')
        break
    
    if username_input == username and password_input == password:
        print('Welcome')
        break
    elif username_input is not username or password_input is not password:
        x += 1
        print('password incorrect please try again')