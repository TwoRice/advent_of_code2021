import numpy as np

def simple_fuel_calc(crab, i):
    return abs(crab - i)

def real_fuel_calc(crab, i):
    distance = simple_fuel_calc(crab, i)
    return int((distance * (distance + 1)) / 2)

def most_efficient_position(crabs, fuel_calc):
    best_fuel = np.inf
    for i in range(crabs.min(), crabs.max()):
        fuel = 0
        for crab in crabs:
            fuel += fuel_calc(crab, i)
        if fuel < best_fuel:
            best_fuel = fuel
    
    return best_fuel

if __name__ == "__main__":
    with open('data/input7.txt', 'r') as f:
        crab_positions = np.array(f.read().split(','), dtype=int)
    
    print(f'Part 1: {most_efficient_position(crab_positions, simple_fuel_calc)}')
    print(f'Part 2: {most_efficient_position(crab_positions, real_fuel_calc)}')