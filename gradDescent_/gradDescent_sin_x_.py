import numpy as np
import matplotlib.pyplot as plt

def y_function(x):
    return np.sin(x)

def y_derivative(x):
    return np.cos(x)

x = np.arange(-5,5,0.1)
y= y_function(x)

init_x = 1.5

current_pos = (init_x, y_function(init_x))

learning_rate = 0.1

for _ in range (1000):
    new_x = current_pos[0] - learning_rate * y_derivative (current_pos[0])
    new_y = y_function (new_x)
    current_pos = (new_x, new_y)

    plt.plot(x,y)
    plt.scatter(current_pos[0],current_pos[1], color ='red')
    plt.pause(0.001)
    plt.clf()

