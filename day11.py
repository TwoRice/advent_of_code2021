import numpy as np

def get_adjecent_indices(coords, shape=(10,10)):
    i, j = coords
    max_i, max_j = shape
    adjecent_square = (
        slice(max(i-1, 0), min(i+2, max_i)), 
        slice(max(j-1, 0), min(j+2, max_j))
    )
    return adjecent_square

def flash(octopuses, flashes):
    while flashes:
        f = flashes.pop()
        np.add.at(octopuses, get_adjecent_indices(f), 1)
        new_flashes = get_flashes(octopuses)
        flashes = flashes.union(new_flashes)
        
def get_flashes(octopuses):
    return set(zip(*np.where(octopuses == 10)))

def iterate(octopuses):
    octopuses = octopuses + 1
    flashes = get_flashes(octopuses)
    flash(octopuses, flashes)
    octopuses[octopuses >= 10] = 0
    return octopuses

if __name__ == "__main__":
    with open('data/input11.txt', 'r') as f:
        octopuses = np.array([list(row) for row in f.read().split('\n')[:-1]], dtype=int)
        
    count = 0
    for i in range(100):
        octopuses = iterate(octopuses)
        count += (octopuses == 0).sum()
    print(f'Part 1: {count}')
    
    count = 0
    while True:
        count += 1
        octopuses = iterate(octopuses)
        if (octopuses == 0).sum() == 100:
            break
    print(f'Part 2: {count + 100}')