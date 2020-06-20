import numpy as np
x = np.array([1,0, 2.4, 3.5, 5.8,10])
print('Print original list: ')
print(x)
print('Checking for complex numbers')
print(np.iscomplex(x))
print('Checking for real numbers')
print(np.isreal(x))
print('Checking for scalar type:')
print(np.isscalar(3.1))
print(np.isscalar([3.1]))

