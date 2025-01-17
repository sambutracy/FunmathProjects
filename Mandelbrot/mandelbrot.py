import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Determine the number of iterations for a given point in the Mandelbrot set.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Compute the Mandelbrot set for a given area and resolution.
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_grid = np.empty((height, width))

    for i in range(height):
        for j in range(width):
            c = x[j] + 1j * y[i]
            mandelbrot_grid[i, j] = mandelbrot(c, max_iter)
    return mandelbrot_grid

# Define the parameters for the Mandelbrot set
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 1000, 1000
max_iter = 100

# Generate the Mandelbrot set
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plot the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_image, extent=(xmin, xmax, ymin, ymax), cmap='hot', interpolation='bilinear')
plt.colorbar(label='Number of iterations')
plt.title('Mandelbrot Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
