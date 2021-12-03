import numpy as np

def bin_to_dec(bin):
    return int(''.join(bin.astype(str)), 2)

def get_rating(rating_data, inverse=False):
    for i in range(rating_data.shape[1]):
        most_common = rating_data[:, i].sum() >= len(rating_data) / 2
        if inverse: most_common = not most_common
        rating_data = rating_data[rating_data[:, i] == most_common]
        if len(rating_data) == 1: break
        
    return rating_data[0]

if __name__ == "__main__":
    with open('data/input3.txt', 'r') as f:
        diagnostic_data = np.array([list(bits.replace('\n', '')) for bits in f], dtype=int)
        
    gamma_rate = diagnostic_data.sum(axis=0) >= 500
    gamma_rate_val = bin_to_dec(gamma_rate.astype(int))
    epsilon_rate = ~gamma_rate
    epsilon_rate_val = bin_to_dec(epsilon_rate.astype(int))
    print(f'Part 1: {gamma_rate_val * epsilon_rate_val}')
    
    oxygen_rate = get_rating(diagnostic_data)
    oxygen_rate_val = bin_to_dec(oxygen_rate)
    co2_rate = get_rating(diagnostic_data, inverse=True)
    co2_rate_val = bin_to_dec(co2_rate)
    print(f'Part 2: {oxygen_rate_val * co2_rate_val}')