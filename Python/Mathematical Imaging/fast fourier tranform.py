
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math 

def fft():

    img = mpimg.imread('./Fig5.26a.jpg')
    M, N = img.shape
    B = np.zeros((M, N))
    F = np.zeros((M, N))
    D = np.zeros((M, N))
    E = np.zeros((M,N))

    for x in range(0, M): 
        for y in range(0, N): 
            B[x][y] = img[x][y]*((-1)**(x+y))

    F = np.fft.fft2(B)
    D = abs(F)

    for x in range(0, M): 
        for y in range(0, N): 
            E[x][y] = math.floor(5*math.log(D[x][y]))
    

    # show spectrum 
    plt.imshow(E, "gray")
    plt.show()

    # average value
    G = abs(np.fft.fft2(img))
    avg = math.floor(G[0][0]/(M*N))
    print(avg)

    # Average intensity value = 138
    # we found the average intensity value by getting the value at F(0,0) (the fourier transform of the image) which is proportional to 
    # the average by a factor of M*N then we divided by M*N to achieve the average
        
fft()