import numpy as np
import pandas as pd

from itertools import product

def get_range(a, b):
    if a > b:
        yield from range(a, b-1, -1)
    else:
        yield from range(a, b+1)

if __name__ == "__main__":
    with open('data/input5.txt', 'r') as f:
        vent_data = f.read().split('\n')[:-1]
    vent_data = np.array([vent.replace(' -> ', ',').split(',') for vent in vent_data], dtype=int)
        
    horz_vents = vent_data[vent_data[:, 0] == vent_data[:, 2]]
    vert_vents = vent_data[vent_data[:, 1] == vent_data[:, 3]]
    non_diag_vents = np.concatenate([horz_vents, vert_vents])
    diag_vents = vent_data[(vent_data[:, 0] != vent_data[:, 2]) & (vent_data[:, 1] != vent_data[:, 3])]
    
    all_points = []
    for vent in non_diag_vents:
        all_points.extend(product(get_range(vent[0], vent[2]), get_range(vent[1], vent[3])))

    points_counts = pd.Series(all_points).value_counts()
    print(f'Part 1:{len(points_counts[points_counts > 1])}')
    
    for vent in diag_vents:
        all_points.extend(zip(get_range(vent[0], vent[2]), get_range(vent[1], vent[3])))
    points_counts = pd.Series(all_points).value_counts()
    print(f'Part 2: {len(points_counts[points_counts > 1])}')