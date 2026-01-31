current_max = None
smallest_num = None

while True:
    enter_numbers = input('Enter numbers: ')
    
    if enter_numbers == '':
        print(f'Largest number: {current_max}')
        print(f'Smallest number: {smallest_num}')
        break
        
    user_num = float(enter_numbers)
    
    if current_max is None:
        current_max = user_num
        smallest_num = user_num
    else:
        if user_num > current_max:
            current_max = user_num

        if user_num < smallest_num:
            smallest_num = user_num