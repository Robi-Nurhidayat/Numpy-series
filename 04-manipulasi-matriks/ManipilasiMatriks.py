import numpy as np

a = np.arange(1,10+1)
 
b = np.array(a)
print(b.reshape(2,5))

b.resize(2,5)
print(b)

print(b.T)

print(b.ravel())
