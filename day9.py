import numpy as np

def compare_adjacent(array, i, j):
    val = array[i, j]
    up = array[i, j+1]
    down = array[i, j-1]
    left = array[i-1, j]
    right = array[i+1, j]
    
    return all([val < adj for adj in [up, down, left, right]])

def check_in_basin(array, i, j, count):
    if array[i, j] < 9:
        array[i, j] = 10
        return find_basin(array, i, j, count = count+1)
    return count

def find_basin(array, i, j, count=0):
    count = check_in_basin(array, i, j+1, count)
    count = check_in_basin(array, i, j-1, count)
    count = check_in_basin(array, i-1, j, count)
    count = check_in_basin(array, i+1, j, count)
        
    return count

if __name__ == "__main__":
    with open('data/input9.txt', 'r') as f:
        height_map = np.array([list(row) for row in f.read().split('\n')[:-1]], dtype=int)
    padded_height_map = np.pad(height_map, 1, constant_values=10)
    
    risk_levels = [
        padded_height_map[i, j] + 1 
        for i in range(1, 101) 
        for j in range(1, 101) 
        if compare_adjacent(padded_height_map, i, j)
    ]
    print(f'Part 1: {sum(risk_levels)}')
    
    basin_sizes = [
        find_basin(padded_height_map.copy(), i, j) 
        for i in range(1, 101) 
        for j in range(1, 101) 
        if compare_adjacent(padded_height_map, i, j)
    ]
    print(f'Part 2: {np.prod(sorted(basin_sizes, reverse=True)[:3])}')