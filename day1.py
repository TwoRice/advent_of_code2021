import numpy as np

def count_increases(data):
    return sum(data[1:] > data[:-1])

if __name__ == "__main__":
    with open('data/input1.txt', 'r') as f:
        sonar_data = np.array([int(line) for line in f])
        
    print(f'Part 1: {count_increases(sonar_data)}')
    windowed_data = np.convolve(sonar_data, np.ones(3, dtype=int), 'valid')
    print(f'Part 2: {count_increases(windowed_data)}')
          
        