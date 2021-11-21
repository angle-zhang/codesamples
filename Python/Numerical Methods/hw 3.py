#%%
import numpy as np

# stopping conditions

def f(x): 
    return x**2 - 4*x + 3

def f1(x):
    return 2*x - 4

def newtons_method(p):
    MAX = 10000
    TOL = 10**-5
    i = 0 
    pn = []
    p0 = p
    p1 = p0
  
    while (i < MAX):
        p1 = p0 - f(p0)/f1(p0)
        pn.append(p1)
        if abs(p1 - p0) < TOL:
            print(pn)
            return p1
        else: 
            p0 = p1
            i += 1
    print(pn)
    return p1

# newtons_method(1.99)
# newtons_method(2.01)

def g(x): 
    return 3*x - np.exp(x)

def secant_method(a, b):
    MAX = 10000
    TOL = 10**-5    
    i = 0
    pn = []
    p0 = a
    p1 = b

    while (i < MAX):
        p = p0 - g(p0)*(p0-p1)/(g(p0) - g(p1))
        pn.append(p)
        if abs(p1 - p0) < TOL:
            print(pn)
            return p1
        else: 
            p0 = p1
            p1 = p
            i += 1
    print(pn)
    return p1

secant_method(1, 2)

# %%
