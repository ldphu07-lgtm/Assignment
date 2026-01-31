def cabin_class():
    user_class = print(input(" What is your cabin class of a cruise ship: "))
    if (user_class == "LUX"):
        print("description: upper-deck cabin with a balcony.")
    elif (user_class == "A"):
        print("description: above the car deck, equipped with a window.")
    elif (user_class == "A"):
        print("description: windowless cabin above the car deck.")
    elif (user_class == "B"):
        print("description: windowless cabin below the car deck.")
    else:
        print("Invalid cabin class")
        
cabin_class()