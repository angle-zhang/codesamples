
import numpy as np 
import matplotlib.pyplot as plt

# h = .1
# y0 = 1
# Hw 5 problem 1
# I = (0, 3)
# h = .1
# y0 = 1
# y1_0 = 2
# y2_0 = 0

# Hw 5 problem 3
I = (0, 2)
hvalues = [.2, .1, .05]
y_a = 0
y_b = -4


def f(x): 
    return x*np.exp(x) - x
    

def exact(y, h):
    tpoints = np.arange(I[0], I[1]+h, h)
    ypoints = y(tpoints)
    return (tpoints, ypoints)

    
# Hw 5 problem 3 
def y(x):
    return 1/6*x**3*np.exp(x) - 5/3*x*np.exp(x) + 2*np.exp(x) - x - 2

def FDM(I, h): 
    N = int((I[1] - I[0]) / h)

    L = np.full(N-2, 30)
    L = np.diag(L, -1)
    U = np.full(N-2, 20)
    U = np.diag(U, 1)
    D = np.full(N-1, -49)
    D = np.diag(D)
    A = L + U + D

    xvalues = np.arange(I[0], I[1]+h, h)
    # print(xvalues, "x")
    F = list(map(f, xvalues[1:N])) #interior points
    F[0] = F[0]+ y_a*(-2/(2*h)-(1/h**2))
    F[N-2] = F[N-2] - y_b*(1/(h**2) -1/h)

    y_i = np.linalg.solve(A, F)
    y_i = np.append(y_i, y_b)
    y_i = np.insert(y_i, 0, y_a)
    return (xvalues, y_i)

R = []
E = []
for h in hvalues:
    R = FDM(I, h)
    E = exact(y, h)
    # calculate errors
    e = E[1] - R[1]
    e_1 = np.sum(np.abs(e))
    e_2 = np.sqrt(np.sum(e**2))
    e_i = np.max(np.abs(e))
    print("h: ", h, "error norm: e 1: ", e_1, "error norm: e 2: ", "error norm: e infinity: ", e_i)
    # plot errors
    plt.scatter(h, e_1, c="green")
    plt.scatter(h, e_2, c="orange")
    plt.scatter(h, e_i, c="purple")

plt.show()
    
# Hw 5 problem 1
# def y(t):
#     return (43/36)*np.exp(t) + (1/4)*np.exp(-t) - (4/9)*np.exp(-2*t) + (t/6)*np.exp(t)

# def v_i1(h, vi, t):
#     B = np.array([0, 0, np.exp(t)])
#     v_s = vi + h*A.dot(vi) + h*B
#     v_i_1 = vi + (h/2)*A.dot(vi)+ (h/2)*B + (h/2)*A.dot(v_s) + (h/2)*B
#     return v_i_1
    
# def bvp(h, I, v0):
#     tpoints = np.arange(I[0], I[1], h)
#     ypoints = [v0[0]]
#     vpoints = v0
#     for t in tpoints:
#         vpoints = v_i1(h, vpoints, t)
#         ypoints = np.append(ypoints, vpoints[0])
    
#     tpoints = np.append(tpoints, I[1])
#     print(ypoints, tpoints)
#     return (tpoints, ypoints)

        
# HW 4

def f(t, y):
    return -5*y + 5*t**2 + 2*t

def y(t):
    return t**2 + 1/3*np.exp(-5*t)

def rk4(f, y0, t, h):
    y = y0
    s1 = f(t, y)
    s2 = f(t+h/2, y + s1*h/2)
    s3 = f(t+h/2, y + s2*h/2)
    s4 = f(t + h, y + h*s3)
    y = y + h*(s1/6 + s2/3 + s3/3 + s4/4)

    return y

def AB2(f, h):
    tpoints = np.arange(I[0], I[1], h)
    ypoints = [y0]
    y = y0
    for i, t in enumerate(tpoints):
        if i < 1:
            y = rk4(f, y, t, h)
        else:
            y = ypoints[i] + h*(3/2*f(t, ypoints[i]) - 1/2*f(tpoints[i-1], ypoints[i-1]))
        ypoints.append(y)

    tpoints = np.append(tpoints, I[1])
    return (tpoints, ypoints)

def AM2(f, h):
    tpoints = np.arange(I[0], I[1], h)
    ypoints = [y0]
    y = y0
    for i, t in enumerate(tpoints):
        if i < 1:
            y = rk4(f, y, t, h)
        else:
            y = (ypoints[i] + h/12*(25*(t+h)**2 + 10*(t+h) + 40*t**2 + 16*t -40*ypoints[i] + 5*ypoints[i-1] -5*tpoints[i-1]**2 - 2*tpoints[i-1]))/(1+25*h/12)
        ypoints.append(y)

    tpoints = np.append(tpoints, I[1])
    return (tpoints, ypoints)
 def f2(t, y):
     return 10*(y-y**2)

 def y(t):
     return np.sin(t)+np.exp(-20*t)

 def approxy(y, t, h):
     return (y + h/2 * (-20*y + 20*np.sin(t) + np.cos(t) + 20*np.sin(t+h) + np.cos(t+h)))/(1+10*h)

 def euler(f, h):
     y = y0
     ypoints = [y]
     tpoints = np.arange(0, 2, h)
     for t in tpoints:
         y = y + h*f(t,y)
         ypoints.append(y)

     tpoints = np.append(tpoints, 2)
     plt.plot(tpoints, ypoints)
     plt.show()

 def trap(h):
     y = y0
     ypoints = [y]
     tpoints = np.arange(0, 2, h)

     for t in tpoints:
         y = approxy(y, t, h)
         ypoints.append(y)

     tpoints = np.append(tpoints, 2)
     plt.plot(tpoints, ypoints)
     plt.show()
    

 def heun(f, h):
     y = .5
     ypoints = [y]
     tpoints = np.arange(0, 5, h)

     for t in tpoints:
         y = y + h/2*(f(t,y) + f(t + h, y + h*f(t, y)))
         ypoints.append(y)

     tpoints = np.append(tpoints, 5)
     plt.plot(tpoints, ypoints)
     plt.show()
        
 rk4(f, h)
 E = exact(y, h)
 heun(f2, .01)
 euler(f, .05)
 trap(.1)
 RES = bvp(h, I, np.array([y0, y1_0, y2_0]))

A = AM2(f, .1)


