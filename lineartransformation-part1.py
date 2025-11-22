#============= Linear Transformation =================
import numpy as np

A = np.array([
    [2,1],
    [0,3]
])

x = np.array([1,2])

TX = A @ x
print(TX)

#Tx = A*X

