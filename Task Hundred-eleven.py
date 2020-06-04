import numpy as np
x = np.array([1,0, np.nan, np.inf])
print('The original list is: ')
print(x)
print(np.isinf(x))
