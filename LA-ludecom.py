
#===================================================LU Decomposition==============================================
import numpy as np
from scipy.linalg import lu

# Matrix A
A = np.array([
    [2, 3, 1],
    [4, 7, 3],
    [6, 18, 5]
])

# Perform LU decomposition
P, L, U = lu(A)

print("Matrix A:\n", A)
print("\nPermutation Matrix P:\n", P)
print("\nLower Matrix L:\n", L)
print("\nUpper Matrix U:\n", U)

# Verify P*A = L*U
left_side = P @ A
right_side = L @ U

print("\nP × A =\n", left_side)
print("\nL × U =\n", right_side)

#Check if both sides are equal
print("\nIs P·A equal to L·U? →", np.allclose(left_side, right_side))
