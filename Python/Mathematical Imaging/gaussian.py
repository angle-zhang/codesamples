
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math 

def lowpass():

    img = mpimg.imread('./Fig4.45(a).jpg')
    M, N = img.shape
    B = np.zeros((M, N))
    F = np.zeros((M, N))
    G = np.zeros((M, N))
    f = np.zeros((M, N))
    g = np.zeros((M, N))
    H = np.zeros((M, N))
    E = np.zeros((M,N))

    # shift 
    for x in range(0, M): 
        for y in range(0, N): 
            B[x][y] = img[x][y]*((-1)**(x+y))

    F = np.fft.fft2(B)

    P = M/2
    Q = N/2

    for u in range(0, M): 
        for v in range(0, N): 
            D = math.sqrt((u-P)**2+(v-Q)**2)
            H[u][v] = math.exp(-(D**2)/1250)
        
    E = np.multiply(F, H)

    f = np.fft.ifft2(E)
    g = abs(f)

    # plt.imshow(g, "gray")
    # plt.show()
        
lowpass()

def highpass():

    img = mpimg.imread('./Fig4.45(a).jpg')
    M, N = img.shape
    B = np.zeros((M, N))
    F = np.zeros((M, N))
    f = np.zeros((M, N))
    g = np.zeros((M, N))
    H = np.zeros((M, N))
    E = np.zeros((M,N))

    # shift 
    for x in range(0, M): 
        for y in range(0, N): 
            B[x][y] = img[x][y]*((-1)**(x+y))

    F = np.fft.fft2(B)

    P = M/2
    Q = N/2

    for u in range(0, M): 
        for v in range(0, N): 
            D = math.sqrt((u-P)**2+(v-Q)**2)
            H[u][v] = 1 - math.exp(-(D**2)/1250)
        
    E = np.multiply(F, H)

    f = np.fft.ifft2(E)
    g = abs(f)

    plt.imshow(g, "gray")
    plt.show()
        
highpass()