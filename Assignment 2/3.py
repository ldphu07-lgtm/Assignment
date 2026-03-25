def user_information():
    sex = input("Your biological sex: ")
    hemoglobin_value = float(input("Your hemoglobin value (g/l): "))
    
    if (sex == "male"):
        if(hemoglobin_value > 167):
            print("Your hemoglobin value is high")
        elif(hemoglobin_value < 134):
            print("Your hemoglobin value is low")
        else:
            print("Your hemoglobin value is normal for an adult male")
    elif (sex == "female"):
        if(hemoglobin_value > 155):
            print("Your hemoglobin value is high")
        elif(hemoglobin_value < 117):
            print("Your hemoglobin value is low")
        else: 
            print("Your hemoglobin value is normal for an adult female")
    else:
        print(" you must enter male or female ")
        
    
user_information()
    