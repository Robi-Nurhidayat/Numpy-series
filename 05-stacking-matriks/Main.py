import numpy as np

a = np.array(([1,2,3],[3,4,5]))
b = np.ones((2,3))

c = np.hstack((a,b))
d = np.vstack((a,b))

g = np.array(([1,1,4],[4,4,5]))
hasil = np.vstack((a,g))

print(a)
print(b)
print(c)

print(hasil)
