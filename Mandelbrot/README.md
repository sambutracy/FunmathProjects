# Mandelbrot Set

The Mandelbrot set is a famous fractal named after the mathematician Benoît B. Mandelbrot. It is a set of complex numbers that produces a distinctive and infinitely complex boundary when plotted on the complex plane.

![Mandelbrot Set](Mandelbrot/Figure_1.png)

## Definition

The Mandelbrot set is defined by the set of complex numbers `c` for which the function `f(z) = z^2 + c` does not diverge when iterated from `z = 0`. In other words, a complex number `c` is part of the Mandelbrot set if the sequence `f(0)`, `f(f(0))`, `f(f(f(0)))`, etc., remains bounded in absolute value.

## Mathematical Formulation

1. Start with a complex number `c`.
2. Initialize `z` to 0.
3. Iterate the function `f(z) = z^2 + c`.
4. If the magnitude of `z` exceeds a certain threshold (typically 2), `c` is not in the Mandelbrot set.
5. If `z` remains bounded after a large number of iterations, `c` is in the Mandelbrot set.

## Visualization

The Mandelbrot set can be visualized by plotting the complex numbers `c` on the complex plane. Points inside the Mandelbrot set are typically colored black, while points outside are colored based on the speed at which they escape to infinity.

### Example Code

Here is an example of how you might generate a Mandelbrot set using Python. This code is provided in multiple Python files within this project for better modularity and reusability.

```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width, height))
    for i in range(width):
        for j in range(height):
            n3[i, j] = mandelbrot(r1[i] + 1j*r2[j], max_iter)
    return (r1, r2, n3)

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height, max_iter = 1000, 1000, 256

r1, r2, n3 = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(n3.T, extent=[xmin, xmax, ymin, ymax], cmap='hot')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.show()
```

Refer to the individual Python files in this project for a more detailed and modular implementation of the Mandelbrot set generation.

## Properties

- **Self-Similarity**: The Mandelbrot set exhibits self-similarity, meaning that zooming into the boundary reveals smaller copies of the entire set.
- **Fractal Dimension**: The boundary of the Mandelbrot set has a fractal dimension, indicating its complex structure.
- **Connection to Julia Sets**: Each point in the Mandelbrot set corresponds to a unique Julia set, another type of fractal.

## Applications

The Mandelbrot set is not just a mathematical curiosity; it has applications in various fields such as:

- **Computer Graphics**: Generating complex and beautiful images.
- **Nature**: Modeling natural phenomena like coastlines and mountain ranges.
- **Art**: Inspiring artists to create intricate and visually appealing designs.

## Further Reading

- [Wikipedia: Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set)
- [Fractals: An Animated Discussion](https://www.youtube.com/watch?v=G_GBwuYuOOs)

## Conclusion

The Mandelbrot set is a fascinating example of how simple mathematical rules can produce incredibly complex and beautiful structures. It continues to be a subject of study and inspiration in both mathematics and art.
