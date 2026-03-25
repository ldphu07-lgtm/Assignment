def leap_year():
    while True:
        year = float(input("enter the year: "))
        if (year % 4 == 0):
            print("It is a leap year")
        elif (year % 100 == 0 and year % 4 == 0):
            print("It is a leap year")
        else:
            print("not a leap year")
leap_year()