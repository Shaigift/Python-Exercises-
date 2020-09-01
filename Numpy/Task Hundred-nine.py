import numpy as np
x = np.array([0,0,0,0,1])
print('Numbers are all zero')
print(np.any(x))
x = np.array([0,0,0,0])
print('Numbers are not all zero')
print(np.any(x))


