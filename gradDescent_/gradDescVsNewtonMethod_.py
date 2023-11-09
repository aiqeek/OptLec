import numpy as np
import matplotlib.pyplot as plt

# Define the quadratic function (f(x) = x^2)
def quadratic_function(x):
    return x**2

# Define the gradient of the quadratic function
def gradient_quadratic_function(x):
    return 2 * x

# Define the Hessian (second derivative) of the quadratic function
def hessian_quadratic_function(x):
    return 2

# Initial guess for both methods
initial_x = 4.0

# Learning rate for gradient descent
learning_rate = 0.1

# Set up the plots
plt.ion()
fig, ax = plt.subplots(figsize=(10, 6))
x = np.linspace(-2, 6, 100)
y = quadratic_function(x)
ax.plot(x, y, 'b-', label="f(x) = x^2")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Newton's Method vs. Gradient Descent")

newton_x = initial_x
gradient_x = initial_x

# Lists to store the history of Newton's method and gradient descent
newton_history = [newton_x]
gradient_history = [gradient_x]

# Create lines for Newton's method and gradient descent
newton_line, = ax.plot(newton_history, [quadratic_function(val) for val in newton_history], 'ro-')
gradient_line, = ax.plot(gradient_history, [quadratic_function(val) for val in gradient_history], 'go-')

# Set labels for the lines
newton_line.set_label("Newton's Method")
gradient_line.set_label("Gradient Descent")

# Main optimization loop
for i in range(10):
    # Newton's method update
    newton_x -= gradient_quadratic_function(newton_x) / hessian_quadratic_function(newton_x)
    newton_history.append(newton_x)

    # Gradient descent update
    gradient_x -= learning_rate * gradient_quadratic_function(gradient_x)
    gradient_history.append(gradient_x)

    # Update the lines
    newton_line.set_data(newton_history, [quadratic_function(val) for val in newton_history])
    gradient_line.set_data(gradient_history, [quadratic_function(val) for val in gradient_history])
    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.legend()
plt.show()

print("Newton's Method solution:", newton_x)
print("Gradient Descent solution:", gradient_x)
