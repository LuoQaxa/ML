import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x1, x2):
    return (14 * 2**(x1**2 + x2**2)) / 3

# Create a grid of x1 and x2 values
x1 = np.linspace(-2, 2, 100)
x2 = np.linspace(-2, 2, 100)
X1, X2 = np.meshgrid(x1, x2)

# Calculate function values
Z = f(X1, X2)

# Create the contour plot
plt.figure(figsize=(8, 6))
contour = plt.contour(X1, X2, Z, levels=20, cmap='viridis')
plt.colorbar(contour)
plt.title('Contour Plot of f(x1, x2) = (14 * 2^(x1^2 + x2^2)) / 3')
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid(True)
plt.show()