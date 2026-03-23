def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

my_list = [10, 20, 30, 40, 50]
result = sum_list(my_list)
print(result)