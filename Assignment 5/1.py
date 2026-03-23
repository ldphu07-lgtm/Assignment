numbers = []

while True:
    num = input("Enter a number (empty to quit): ")
    if num == "":
        break
    numbers.append(float(num))

numbers.sort(reverse=True)
print(numbers[:5])