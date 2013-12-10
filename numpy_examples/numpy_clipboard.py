import numpy as np
import matplotlib.pyplot as plt

A = np.array( [[1,1],
            [0,1]])
B = np.array( [[2,0],
            [3,4]])

print 'Elementwise Multiplication A*B'
print A*B

print 'Matrix Multiplication dot(A,B)'
print np.dot(A,B)
