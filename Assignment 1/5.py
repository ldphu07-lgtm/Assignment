print("give me 3 integer numbers and i'll give you a sum, product, and average of those")

while True:
    try:
        
        n1 = int(input("input first number: "))
        n2 = int(input("input second number: "))
        n3 = int(input("input third number: "))
        break
    
    except ValueError:
        print("\n The number is not an integer number, please try again. \n")

sum = str(n1 + n2 + n3)
product = str(n1 * n2 * n3)
average = str(int(sum) / 3)

print("sum of those: " + sum)
print("product of those: " + product)
print("average of those: " + average)