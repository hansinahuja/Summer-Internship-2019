# Libraries to plot a graph
import numpy as np
import matplotlib.pyplot as plt

# Function to compute derivative
def derivative(x):
    x_deriv = 3* (x**2) - (6 * (x))
    return x_deriv

function = lambda x: (x ** 3)-(3 *(x ** 2))+7 # The function we'll be minimizing

# Initializing the hyperparamters
precision = 0.001
learning_rate = 0.05

# Initialising with random values
x_new = np.random.rand()
x_old = np.random.rand()

# To plot the graph
x_list = [x_new]
y_list = [function(x_new)]
x = np.linspace(-1,3,500)

# Running gradient descent
while(abs(x_new-x_old) > precision):
    x_old = x_new
    dx = derivative(x_old)
    x_new = x_old - (learning_rate * dx)
    x_list.append(x_new)
    y_list.append(function(x_new))

# Plotting the graph and printing results
print ("Local minimum occurs at: "+ str(x_new))
print ("Number of steps: " + str(len(x_list)))
plt.subplot(1,2,2)
plt.scatter(x_list,y_list,c="g")
plt.plot(x_list,y_list,c="g")
plt.plot(x,function(x), c="r")
plt.title("Gradient descent")
plt.show()
