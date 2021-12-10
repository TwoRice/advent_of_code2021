if __name__ == "__main__":
    with open('data/input10.txt', 'r') as f:
        chunks = f.read().split('\n')[:-1]
        
    char_map = {'(':')', '[':']', '{':'}', '<':'>'}
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
    
    error_score = 0
    error_idx = []
    for i, line in enumerate(chunks):
        active_open_chars = []
        for char in line:
            if char in char_map:
                active_open_chars.append(char)
            else:
                last_open_char = active_open_chars.pop()
                if char_map[last_open_char] != char:
                    error_score += score_map[char]
                    error_idx.append(i)
                    break
                    
    print(f'Part 1: {error_score}') 
    
    valid_lines = [chunks[i] for i in range(len(chunks)) if i not in error_idx]
    score_map = {'(': 1, '[': 2, '{': 3, '<': 4}
    
    line_scores = []
    for line in valid_lines:
        score = 0
        active_open_chars = []
        for char in line:
            if char in char_map:
                active_open_chars.append(char)
            else:
                active_open_chars.pop()
        for char in active_open_chars[::-1]:
            score = score*5 + score_map[char]
        line_scores.append(score)
        
    print(f'Part 2: {sorted(line_scores)[int(len(valid_lines) / 2)]}')