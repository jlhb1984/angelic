import numpy as np
from numpy.random import binomial
from scipy.stats import binom
from math import factorial
import matplotlib.pyplot as plt

class Bernoulli:
    k=float
    n=float
    p=float

    def __init__(self,k,n,p):
        self.k=k
        self.n=n
        self.p=p

    def calculate_bernoulli(k,n,p):
        dist=binom(n,p)
        pmf=dist.pmf(k)
        cdf=dist.cdf(k)
        print("pmf= ",pmf)
        print("cdf= ",cdf)

