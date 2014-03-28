import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10)
line = plt.plot(x,np.sin(x),'-',linewidth = 2)
plt.show()
