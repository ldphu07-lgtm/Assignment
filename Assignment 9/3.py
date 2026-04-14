def convert_to_uppercase(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open('output.txt', 'w', encoding='utf-8') as f_out:
        f_out.write(content.upper())
    print("Đã lưu nội dung chữ hoa vào file output.txt")