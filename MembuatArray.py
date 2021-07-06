import numpy as np

# input 

# vector
vector = np.array([1,2,3])

# membuat vector dengan range

vectorDenganRange = np.arange(1,10,3)

# membuat linspace
sebuahLinspace = np.linspace(1,10,4)


# array multidimensi
arrayMultiDimensi = np.array([(1,2,3),(1,4,5)])

# matrix dengan nilai nol

nilaiNol = np.zeros((2,4))


# matrix dengan nilai 1

nilaiSatu = np.ones((3,4))


# matrix identitas

identitas1 = np.identity(4)
identitas2 = np.eye(3)

# output

print(vector)
print(vectorDenganRange)
print(sebuahLinspace)
print(arrayMultiDimensi * 2)
print(nilaiNol)
print(nilaiSatu)
print(identitas1)
print(identitas2)