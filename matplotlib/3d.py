# multivariate functions

import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x1, x2)
def f(x1, x2):
    return (14 + 2 * x1**2 + x2**2) / 3

# Generate a range of values for x1 and x2
# arguments: start, stop, number
x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)

# Create a meshgrid for x1 and x2 values
# generate 100 * 100 matrix, use generate all possible point, example the first point X1[0][0], X2[0][0]
# means x1 = -5, x2 = 5 composition.
X1, X2 = np.meshgrid(x1, x2)

Z = f(X1, X2)  # Calculate f(x1, x2) for each pair of (x1, x2)

# Create the 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Z, cmap='viridis', edgecolor='k', alpha=0.7)

# Label the axes
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x1, x2)')
ax.set_title(r'$f(x_1, x_2) = \frac{14 + 2x_1^2 + x_2^2}{3}$')

# Show the plot
plt.show()
