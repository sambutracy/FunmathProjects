import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numba import jit

@jit
def mandelbrot(c, max_iter):
    """
    Determine the number of iterations for a g
pip install numbaiven point in the Mandelbrot set.
    Accelerated with Numba for faster computation.
    """
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

@jit
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Compute the Mandelbrot set for a given area and resolution.
    Accelerated with Numba for faster computation.
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mandelbrot_grid = np.empty((height, width))

    for i in range(height):
        for j in range(width):
            c = x[j] + 1j * y[i]
            mandelbrot_grid[i, j] = mandelbrot(c, max_iter)
    return mandelbrot_grid

# Define parameters for the Mandelbrot set
width, height = 600, 600  # Reduced resolution for faster computation
max_iter = 100  # Lower iteration count for quicker frame generation
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis('off')  # Turn off axis labels
im = ax.imshow(
    mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter),
    extent=(xmin, xmax, ymin, ymax),
    cmap='hot',
    interpolation='bilinear'
)

# Update function for the animation
def update(frame):
    global xmin, xmax, ymin, ymax
    zoom_factor = 0.90  # Increased zoom factor for faster zoom
    dx = (xmax - xmin) * (1 - zoom_factor) / 2
    dy = (ymax - ymin) * (1 - zoom_factor) / 2
    xmin += dx
    xmax -= dx
    ymin += dy
    ymax -= dy

    # Update the image with the new Mandelbrot set
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    im.set_array(mandelbrot_image)
    im.set_extent((xmin, xmax, ymin, ymax))
    return [im]

# Create the animation
anim = FuncAnimation(fig, update, frames=100, interval=50, blit=True)  # Reduced frame count to 100

# Save the animation as a video or GIF
# Uncomment the following lines to save:
# anim.save('mandelbrot_zoom.mp4', fps=30, dpi=150)
anim.save('mandelbrot_zoom.gif', fps=30, dpi=150, writer='pillow')

# Show the animation
plt.show()
