import random
number = random.randint(1, 10)

while True:
    user_num = int(input((f'Guess the number (1-10): ')))
    try:
        if user_num > number:
            print('Too high')
        elif user_num < number:
            print('Too low')
        elif user_num == number:
            print('correct')
            break
    except:
        print('please enter integer')