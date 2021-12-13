import numpy as np

def fold(dots, axis, f):
    for i in range(len(dots)):
        if dots[i, axis] > f:
            dots[i, axis] = f - (dots[i,axis] - f)
    return dots

def plot(coords):
    max_i, max_j = coords.max(axis=0)
    page = np.ones((max_i+1, max_j+1), int)
    for coord in coords:
        page[coord[0], coord[1]] = 0
    return page.T

if __name__ == "__main__":
    with open('data/input13.txt', 'r') as f:
        instructions = f.read().split('\n')[:-1]
    coords = np.array([tuple(coord.split(',')) for coord in instructions[:-13]], dtype=int)
    folds = [(0 if instruction[11] == 'x' else 1, int(instruction[13:])) for instruction in instructions[-12:]]
    
    first_fold = folds[0]
    folded_coords = fold(coords, first_fold[0], first_fold[1])
    print(f'Part 1: {len(set(map(tuple, folded_coords)))}')
    
    folded_coords = coords.copy()
    for f in folds:
        folded_coords = fold(folded_coords, f[0], f[1])
        
    np.set_printoptions(edgeitems=30, linewidth=100000, formatter=dict(float=lambda x: "%.3g" % x))
    print(f'Part 2:\n{plot(folded_coords)}')