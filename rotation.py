import numpy as np

theta = np.pi/2
Q = np.array([
    [np.cos(theta),-np.sin(theta)],
    [np.sin(theta),np.cos(theta)]
])
x=np.array([1,0])
print(Q@x)

