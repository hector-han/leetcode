import numpy as np


def get_prob(n, sample_time=100000):
    sum = 0
    for i in range(sample_time):
        samples = np.random.rand(n)
        min_val = np.min(samples)
        max_val = np.max(samples)
        if max_val - min_val <= 0.5:
            sum += 1
        else:
            slice_1 = np.where(samples <= 0.5)
            slice_1 = samples[slice_1]
            slice_2 = np.where(samples >= 0.5)
            slice_2 = samples[slice_2]
            if np.max(slice_1) + 1 - np.min(slice_2) <= 0.5:
                sum += 1
    return sum / sample_time


if __name__ == '__main__':
    for i in range(1, 10):
        print(i, get_prob(i), i/(2**(i-1)))