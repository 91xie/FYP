from numpy import *
from numpy.linalg import *

a = array( [[1,1],
            [0,1]])
b = array( [[2,0],
            [3,4]])
y = array ([[1],
            [2]])
print 'Elementwise Multiplication A*B'
print a*b

print 'Matrix Multiplication dot(A,B)'
print dot(a,b)


print 'a.transpose()'
print a.transpose()

print 'inv(a)'
print inv(a)

print 'solve(a,y)'
print solve(a,y)
