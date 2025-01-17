import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numba import jit

@jit
def mandelbrot(c, max_iter):
    """
    Escape time algorithm: calculates the iteration count at which
    the point escapes the Mandelbrot set.
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
    Compute the Mandelbrot set using the escape time algorithm.
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
width, height = 600, 600
max_iter = 100
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.axis('off')  # Turn off axis labels
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
im = ax.imshow(
    mandelbrot_image,
    extent=(xmin, xmax, ymin, ymax),
    cmap='hot',  # Initial colormap
    interpolation='bilinear'
)

# Update function for the animation
def update(frame):
    global xmin, xmax, ymin, ymax, max_iter
    zoom_factor = 0.90
    dx = (xmax - xmin) * (1 - zoom_factor) / 2
    dy = (ymax - ymin) * (1 - zoom_factor) / 2
    xmin += dx
    xmax -= dx
    ymin += dy
    ymax -= dy

    max_iter += 5  # Gradually increase iterations for more detail

    # Compute the Mandelbrot set for the new zoomed area
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    # Choose a colormap based on the frame number
    cmap_options = ['hot', 'plasma', 'inferno', 'viridis']
    im.set_cmap(cmap_options[frame % len(cmap_options)])
    im.set_array(mandelbrot_image)
    im.set_extent((xmin, xmax, ymin, ymax))
    return [im]

# Create the animation
anim = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Save the animation as a GIF
anim.save('mandelbrot_escape_time.gif', fps=30, dpi=150, writer='pillow')

# Show the animation
plt.show()
