import re

def is_valid_hex_color():
    pattern = r'^#[0-9a-fA-F]{6}$'
    if re.match(pattern, user_color):
        print("true")
    else:
        print("false")

user_color = input("your hex_color code: ")
is_valid_hex_color()