import numpy as np
from numpy.linalg import det

a = np.array(([1,2,3],[1,2,3],[1,2,3]))
b = np.array([(1,2,3),[1,2,3]])
c = np.array(([1,1],[-1,1]))

d = np.array(([2,1],[-2,1]))

print(a)
print(b)

# invers matrik



# a_inv = np.linalg.inv(a)
# print(a_inv)

# b_inv = np.linalg.inv(b)
# print(b_inv)

c_inv = np.linalg.inv(c)
print(c_inv)

d_inv = np.linalg.inv(d)
print(d_inv)

# determinan

c_det = np.linalg.det(c)
c_det_inv = np.linalg.det(c_inv)

print(c_det)
print(c_det_inv)


d_det = np.linalg.det(d)
d_det_inv = np.linalg.det(d_inv)
print(d_det)
print(d_det_inv)