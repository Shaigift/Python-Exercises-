import numpy as np
x = np.array([1,0, np.nan, np.inf])
print('Original array')
print(x)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(x))



