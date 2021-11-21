import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math 
import skimage

f_xy = mpimg.imread('./Fig5.07(a).jpg')
g_xy = np.copy(f_xy)
g_xy = skimage.util.random_noise(f_xy, mode='gaussian', mean=0, var=.01)
height, width = g_xy.shape

fp_xy = np.zeros((height, width))

def SNR(normal, denoised): 
    # normalize normal
    normal = normal/255
    numer = np.sum(np.square(denoised))
    denom = np.sum(np.square(np.subtract(normal, denoised)))
    return 10*np.log10(numer/denom)

print("before denoising SNR = {}".format(SNR(f_xy, g_xy)))

# average for m mask
def arithmetic_mean_filter():  
    avg = 1/9

    sum = 0
    for i in range(3, height-2): 
        for j in range(3, width-2): 
            temp = g_xy[i-1:i+2,j-1:j+2]
            sum = avg*np.sum(temp)
            fp_xy[i][j] = sum
    
    # plt.imshow(fp_xy, "gray")
    # plt.show()

    # before noise SNR
    print("arithmetic denoised SNR = {}".format(SNR(f_xy, fp_xy)))

def geometric_mean_filter():  
    power = 1./9.

    for i in range(3, height-2): 
        for j in range(3, width-2): 
            temp = g_xy[i-1:i+2,j-1:j+2]
            a = np.log(temp) # for overflow
            fp_xy[i][j] = np.exp(np.sum(a)*power)
    
    # plt.imshow(fp_xy, "gray")
    # plt.show()
    # denoised SNR
    print("geometric denoised SNR = {}".format(SNR(f_xy, fp_xy)))

arithmetic_mean_filter()
geometric_mean_filter()
        
