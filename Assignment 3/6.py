def extract():
    given_string = input('Enter a word: ')
    length = len(given_string)
    middle = length // 2
    
    if length % 2 == 0:
        print(given_string[middle - 1:middle + 1])
    else:
        length = float(len(given_string))
        print(given_string[middle])
        
extract()
