import matplotlib.pyplot as plt
import numpy as np

x = np.arange(6) #returns 0, 1, 2, 3, 4 ,5
y = np.arange(5)
#y[:,np.newaxis] y transposed
z = x * y[:,np.newaxis] 

for i in xrange(5):
    if i==0:
        p = plt.imshow(z)
        fig = plt.gcf()
        plt.clim()   # clamp the color limits
        plt.title("Boring slide show")
    else:
        z = z + 2
        p.set_data(z)

    print("step", i)
    plt.pause(0.5)
