import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math 

f1_xy = mpimg.imread('./Fig5.08(a).jpg')
f2_xy = mpimg.imread('./Fig5.08(b).jpg')

height, width = f1_xy.shape

def contraharmonic_filter(q, f_xy):
    fp_xy = np.zeros((height, width), dtype=np.longdouble)

    for i in range(3, height-2): 
        for j in range(3, width-2): 
            temp = np.copy(f_xy[i-1:i+2,j-1:j+2])
            t_temp = temp.astype(dtype=np.longdouble)
            t_temp[t_temp == .0] = .0000001
            num = np.sum(t_temp**(q+1))
            den = np.sum(t_temp**(q))
            fp_xy[i][j] = num/den
    
    
    
    plt.imshow(fp_xy, "gray")
    plt.show()


# contraharmonic_filter(1.5, f1_xy)
contraharmonic_filter(-1.5, f2_xy)