import numpy as np

#!vector
# v=np.array([1,2,3])
# print(v)

#!Matrix
#?@ is used for matrix multiplication
# A=np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# #  

# print()

# B=np.array([
#     [7,8],
#     [9,10],
#     [1,2]
# ])
# print(B)

print()

#!Matrix multiplication
# AxB = A @ B
# print(AxB)

#!Scalar multiplication
# vector_scaled = 10*v
# print(vector_scaled)

#!Transpose of a matrix
# trans_A=A.T
# print(trans_A)

#!Equation of matrix
#? i)2x+3y = 8 ,
#? ii)5x+4y = 13
#? b=[8,13]



#...existing code...

a = np.array([
    [2,3],
    [5,4]
])

b = np.array([8, 13])

x = np.linalg.solve(a, b)
print(x)