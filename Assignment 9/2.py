def find_keyword_lines(file_path, keyword):
    line_numbers = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if keyword in line:
                line_numbers.append(i)
    return line_numbers