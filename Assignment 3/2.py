def converter():
    while True:
            inch = float(input("Enter inches: "))
            if inch < 0:
                print("vui lòng nhập số hợp lệ")
                break
            centimeter = inch * 2.54
            print(f'centimeters: {centimeter}')
      
converter()
        