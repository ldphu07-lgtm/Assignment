import re

def redact_phone_numbers(document):
    
    pattern = r'(\+84\d+|\b\d{10}\b)'
    
    return re.sub(pattern, "[REDACTED]", document)

text = input("Enter: ")
result = redact_phone_numbers(text)

print("Văn bản đã ẩn:", result)