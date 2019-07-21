#Function to calculate no. of points incorrectly separated
def error(points, w, b):
    err = 0
    for point in points:
        temp = (point[0]*w[0] + point[1]*w[1]) + b
        if temp >= 0:
            predicted_ans = 1
        else:
            predicted_ans = 0
        if predicted_ans != point[2]:
            err += 1
    return err


#Input section
n = int(input("Enter number of coordinates: "))
points = list()
print("Enter coordinates followed by its label (0/1): ")
for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)
iterations = int(input("Enter number of learning iterations: "))

#Initialise w, b with random values and 0<r<1
w = [0, 0]
b = 0
r = 0.1

#Learning loop
while iterations!=0:
    for point in points:
        temp = (point[0]*w[0] + point[1]*w[1]) + b
        if temp >= 0:
            predicted_ans = 1
        else:
            predicted_ans = 0

        w[0] += r * (point[2] - predicted_ans) * point[0]
        w[1] += r * (point[2] - predicted_ans) * point[1]
        b += r * (point[2] - predicted_ans)

    iterations -= 1

#Calculating the error
err = error(points, w, b)
err_percentage = (err/n)*100

#Printing section
if w[1] != 0:
    m = w[0]/w[1]
    c = -b/w[1]
    print("The linear separator is: y = " + str(m) + "x + " + str(c))
else:
    m = w[0]
    c = -b
    print("The linear separator is: " + str(m) + "x + " + str(c) + " = 0")
print("Error percentage = " + str(err_percentage) + "%")
