import numpy as np

def find_5(six, fives):
    for pattern in fives:
        if all([x in six for x in pattern]):
            return pattern
        
def sort_string(string):
    return ''.join(sorted(string))

def compare_patterns(a, b, inverse=False):
    for pattern in b:
        if not all([x in pattern for x in a]) == inverse:
            return pattern

def get_patterns_map(patterns):
    patterns_map = {patterns[2][0]: 1, patterns[3][0]: 7, patterns[4][0]: 4, patterns[7][0]: 8}
    
    six = compare_patterns(patterns[2][0], patterns[6], inverse=True)
    patterns_map[six] = 6
    patterns[6].remove(six)
    
    three = compare_patterns(patterns[2][0], patterns[5])
    patterns_map[three] = 3
    patterns[5].remove(three)
    
    five = find_5(six, patterns[5])
    patterns_map[five] = 5
    patterns[5].remove(five)
    
    nine = compare_patterns(three, patterns[6])
    patterns_map[nine] = 9
    patterns[6].remove(nine)
    
    patterns_map[patterns[5][0]] = 2
    patterns_map[patterns[6][0]] = 0
    
    return patterns_map

def read_output(output, patterns_map):
    return int(''.join([str(patterns_map[x]) for x in output]))

if __name__ == "__main__":
    with open('data/input8.txt', 'r') as f:
        input_data = [display.split(' ') for display in f.read().split('\n')[:-1]]
    signal_patterns = []
    outputs = []
    for display in input_data:
        signal_patterns.append([sort_string(x) for x in display[:10]])
        outputs.append([sort_string(x) for x in display[11:]])
    
    signal_patterns_len_map = []
    for patterns in signal_patterns:
        patterns_map = {}
        for pattern in patterns:
            pattern_len = len(pattern)
            patterns_map[pattern_len] = patterns_map.get(pattern_len, []) + [pattern]
        signal_patterns_len_map.append(patterns_map)
        
    part1 = len([length for output in outputs for length in map(len, output) if length in [2, 3, 4, 7]])
    print(f'Part 1: {part1}')
    
    corrected_outputs = []
    for len_map, output in zip(signal_patterns_len_map, outputs):
        pattern_map = get_patterns_map(len_map)
        corrected_outputs.append(read_output(output, pattern_map))
    print(f'Part 2: {sum(corrected_outputs)}')