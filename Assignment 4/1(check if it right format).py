code = input("Enter your course: ")
def is_valid_course(code):
    if len(code) != 6:
        return False
    
    letters = code[:3]  
    digits = code[3:]   
    
    if letters.isalpha() and letters.isupper() and digits.isdigit():
        return True
    else:
        return False
is_valid_course(code)