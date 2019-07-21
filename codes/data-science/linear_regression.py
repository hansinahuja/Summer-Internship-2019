import numpy as np   # To carry out matrix operations

# Input section
n = int(input("Enter number of coordinates: "))
A = []
b = []
print("Enter coordinates:")
for i in range(n):
    point = list(map(int, input().split()))
    A.append([point[0], 1])
    b.append(point[1])

# Calculation of slope and y-intercept using least squares method
A = np.array(A)
b = np.reshape(np.array(b), (len(b), 1))
A_star = np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)
X = np.dot(A_star, b)

# Printing section
print("The required line is:")
if(X[1][0]<0):
    print("y =", X[0][0], "x -", abs(X[1][0]))
else:
    print("y =", X[0][0], "x +", X[1][0])
