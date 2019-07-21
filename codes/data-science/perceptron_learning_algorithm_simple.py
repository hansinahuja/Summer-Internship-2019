#input section
n = int(input("Enter number of coordinates: "))
points = list()
print("Enter coordinates followed by its label (0/1): ")
for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)

#forming the vectors 3 dimensional vectors
vectors = []
for point in points:
    if point[2]==0:
        vector = [-point[1], -point[0], 1]
    else:
        vector = [point[1], point[0], -1]
    vectors.append(vector)

#initialise w to a random vector
w = [1, 1, 1]

#loop section
i=0
while i<n:
    x = vectors[i]
    dot = (x[0]*w[0]) + (x[1]*w[1]) + (x[2]*w[2])
    if dot<=0:
        w[0] += x[0]
        w[1] += x[1]
        w[2] += x[2]
        i=0
    else:
        i+=1

#printing section
print("The line is:")
print("y = ", -w[1]/w[0], end="")
print("x +", w[2]/w[0])
