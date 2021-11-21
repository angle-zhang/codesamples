# [2] approximate f'(x) with forward difference formula
import numpy as np
import math
k_vals = np.arange(2, 13, 2)
h_vals = [math.pow(10, -k) for k in k_vals]

# function def
def f(x): 
    return math.exp(x)

real = 1 
fwd_differences = [(f(h)-f(0))/h for h in h_vals]
abs_errors = [abs(real - approx) for approx in fwd_differences]


print(fwd_differences)
print(abs_errors)
