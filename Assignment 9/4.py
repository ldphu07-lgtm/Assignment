def calculate_average_score(file_path):
    total_score = 0
    count = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) == 2:
                    score = float(parts[1])
                    total_score += score
                    count += 1
    
    if count == 0:
        return 0
    return total_score / count