import numpy as np

def increment(fish):
    fish = np.roll(fish, shift=-1)
    fish[6] += fish[8]
    return fish

def count_fish(fish_data, days):
    fish_days = np.array([0] * 9)
    for fish in fish_data:
        fish_days[fish] += 1
        
    for i in range(days):
        fish_days = increment(fish_days)
        
    return sum(fish_days)

if __name__ == "__main__":
    with open('data/input6.txt', 'r') as f:
        fish_data = np.array(f.read().split(','), dtype=int)
        
    fish = count_fish(fish_data, 80)
    print(f'Part 1: {fish}')
        
    fish = count_fish(fish_data, 256)
    print(f'Part 2: {fish}')