import random

def clipped_normal(mean, stdev, thresh=None):
    if thresh is None:
        thresh = mean

    value = random.gauss(mean, stdev)
    if (value < mean - thresh) or (value > mean + thresh):
        value = random.uniform(mean - thresh, mean + thresh)
    value = round(value, 6)

    return value
