import numpy as np


class NormalDist:
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def __add__(self, dist):
        return NormalDist(self.mu + dist.mu, self.sigma + dist.sigma)

    def __sub__(self, dist):
        return NormalDist(self.mu - dist.mu, self.sigma + dist.sigma)

    def get_samples(self, size):
        return np.random.normal(self.mu, self.sigma, size)
