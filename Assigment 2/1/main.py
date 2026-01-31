def askFisher():
    while True:
        size = float((input("What is the length of Zander (cm): ")))
        if (size >= 42):
            try:
                print(" Zander is qualified ")
            except:
                print(" syntax error ")
        elif (size < 42 and size > 0):
            print(" release the fish back into the lake")
            
            print(f"The fish is {42-size} centimeters below the size limit")

askFisher()