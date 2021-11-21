

import numpy as np 
import matplotlib.pyplot as plt

h_values = [.1, .05, .025] 

def f(t,y): 
    return -5*y + 5*(t**2) + 2*t

def eulers(y0, h, t0, T):
    t_values = np.arange(t0, T+h, h)
    y_values = [y0]
    y_i = 0

    for t in t_values[1:]: 
        y_values.append(y_values[y_i] + h*f(t, y_values[y_i]))
        y_i =+ 1

    print(t_values, y_values)

    plt.plot(t_values, y_values)
    plt.show()

       
for h in h_values:
    eulers(1/3, h, 0, 1)