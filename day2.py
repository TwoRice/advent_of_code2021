import numpy as np

if __name__ == "__main__":
    with open('data/input2.txt', 'r') as f:
        nav_instructions = [instruction.split(' ') for instruction in f]
        
    coords = [0, 0]
    for instruction in nav_instructions:
        if instruction[0] == 'forward':
            coords[0] += int(instruction[1])
        elif instruction[0] == 'up':
            coords[1] -= int(instruction[1])
        else:
            coords[1] += int(instruction[1])
    print(f'Part 1: {coords[0] * coords[1]}')
    
    coords = [0, 0, 0] # aim horiontal depth
    for instruction in nav_instructions:
        if instruction[0] == 'up':
            coords[0] -= int(instruction[1])
        elif instruction[0] == 'down':
            coords[0] += int(instruction[1])
        else:
            coords[1] += int(instruction[1])
            coords[2] += int(instruction[1]) * coords[0]
    print(f'Part 2: {coords[1] * coords[2]}')