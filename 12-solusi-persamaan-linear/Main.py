import numpy as np

a = np.array([(2,3),(1,2)])
Y = np.array([23,14])

print(a)
print(Y)

# menentukan nilai x nya berapa di ajabar linear

# iverskan dahulu a

a_inv = np.linalg.inv(a)

# kemudian hasil invers dikali dengan Y

X = np.dot(a_inv,Y)
print(X)

# cara lain

# menggunakan metode solved

Xbaru = np.linalg.solve(a,Y)
print(Xbaru)