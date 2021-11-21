import numpy as np
import math

n_vals = [10, 20, 40, 80,85000]
actual = 3*np.log(3/2) + 1/2 -2

def f(x): 
    return (x**2-1)/(x+2)

# TRAPEZOID RULE
# for n in n_vals: 
#     h = 1/(n+2)
#     x = np.arange(0+h, 1, h)
#     result = f(x[0])
#     for i in range(1,n): 
#         result += 2*f(x[i])
#     result += f(x[n])
#     result *= h/2
#     print("result: ")
#     print(n, result)
#     print("abs error")
#     print(result - actual)
#     print("abs error x n2")
#     print((result - actual)*(n**2))

# SIMPSON'S RULE
for n in n_vals: 
    h = 1/n
    x = np.arange(0, 1+h, h)
    result = f(x[0])
    for i in range(1,n): 
        if i%2: 
            result += 4*f(x[i])
        else: 
            result += 2*f(x[i])
    result += f(x[n])
    result *= h/3
    # print("result: ")
    # print(n, result)
    # print("abs error")
    # print(result - actual)
    print("abs error x n2")
    print((result - actual)*(n**4))
