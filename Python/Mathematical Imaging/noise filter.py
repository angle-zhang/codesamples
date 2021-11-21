#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import io
import numpy as np

def padding(offset, array, image): 
    array[offset:image.shape[0]+offset, offset:image.shape[1]+offset] = image
    return array

# linear average filter
def noise_filter(m):  
    origin_image = mpimg.imread('./Fig0335(a).tif')
    w,h = origin_image.shape
    a = (m - 1)//2
    nw, nh = (m-1, m-1)
    # add image padding
    f_xy = padding(a, np.zeros((w+nw,h+nh)), origin_image)
    # print(f_xy.shape)

    # resulting image 
    g_xy = np.zeros((w+nw,h+nh))

    mask = np.zeros((m,m))

    # start from first number
    for x in range(a, a + w):
        for y in range(a, a + h):
            for s in range(-a, a+1, 1): 
                for t in range(-a, a+1, 1):
                    mask[s+a][t+a] = f_xy[x+s][y+t]
                    # print(s, t, mask[s+a][t+a], f_xy[x+s][y+t])
            med_list = mask.flatten()
            med_list.sort()
            g_xy[x][y] = med_list[4]

    w = 1/(m*m)
    g_xy = np.floor(g_xy*w)
    plt.imshow(g_xy, "gray")
    plt.show()

# average for m image
def spatial_filter(m):  
    origin_image = mpimg.imread('./Fig0335(a).tif')
    w,h = origin_image.shape
    a = (m - 1)//2
    nw, nh = (m-1, m-1)
    
    # add image padding
    f_xy = padding(a, np.zeros((w+nw,h+nh)), origin_image)
    # resulting image 
    g_xy = np.zeros((w+nw,h+nh))
    # start from first number
    for x in range(a, a + w ):
        for y in range(a, a + h ):
            for s in range(a, -a - 1, -1): 
                for t in range(a, -a - 1, -1):
                    g_xy[x][y] += f_xy[x+s][y+t]

    w = 1/(m*m)
    g_xy = np.floor(g_xy*w)
    plt.imshow(g_xy, "gray")
    plt.show()
    
def show_original():
    origin_image = mpimg.imread('./Fig0335(a).tif')
    plt.imshow(origin_image, "gray")
    plt.show()

show_original()
noise_filter(3)
spatial_filter(3)

     

# %%
