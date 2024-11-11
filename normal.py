import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class Normal:
    x=float
    mu=float
    sigma=float

    def __init__(self,x,mu,sigma):
        self.x=x
        self.mu=mu
        self.sigma=sigma
        
    def calculate_normal(x,mu,sigma):
        dist=norm(mu,sigma)
        print("pdf: ",dist.pdf(x))
        print("cdf: ",dist.cdf(x))