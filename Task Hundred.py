import numpy as np
x = np.array([1,0, np.nan, np.inf])
print('The original number is: ')
print(x)
print('Test element-wise for NaN:')
print(np.isnan(x))


