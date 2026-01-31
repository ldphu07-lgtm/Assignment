def acronym_converter():
    phrase = input('Enter phrase: ')

    words = phrase.split()
    
    acronym = ""
    for word in words:
        character = word[0].upper() 
        acronym = acronym + character
    
    print(f'{acronym}')

acronym_converter()