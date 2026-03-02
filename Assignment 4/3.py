import re

def sum_numbers_in_text(input_text):
    pattern = r'\d+\.?\d*'
    
    numbers = re.findall(pattern, input_text)
    
    total = sum(float(num) for num in numbers if num != '')
    return total

input_text = input("Enter your sentence: ")
result = sum_numbers_in_text(input_text)

print(f"summary: {result}")