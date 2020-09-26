import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_point(x: float, y: float, iterations: int, threshold: int) -> int:
    """
    Given an x-value, y-value, maximum_iterations, and a divergence threshold
    this function will return at which iteration the function diverges.
    If it does not diverse, it will return 0
    """
    c = np.complex(x, y)
    z = c
    for i in range(iterations):
        z = z**2 + c
        if abs(z) > threshold:
            return i
    return 0


def generate_mandelbrot(pixel_density: int = 1000, max_iterations: int = 255, threshold: int = 4) -> None:
    """
    This function will generate a mandelbrot plot using matplotlib.

    The pixel_density determines how many pixels will be along the images length and width.
    The maximum iterations is how many interations the mandelbrot function will execute
    before determining that it will not diverge. The threshold value is the value at which
    the mandelbrot function is considered divergent.

    Mandelbrot Set: Z_(n) = (Z_(n-1))**2 + c, where Z_(0) = c
    """
    # Initializing values
    x_vals = np.linspace(-2, 0.47, pixel_density)
    y_vals = np.linspace(-1.12, 1.12, pixel_density)
    mandelbrot_array = np.empty((len(x_vals), len(y_vals)))

    for i, x in enumerate(x_vals):
        for j, y in enumerate(y_vals):
            mandelbrot_array[i, j] = 200 - mandelbrot_point(x, y, max_iterations, threshold)

    plt.imshow(mandelbrot_array, cmap='magma', interpolation='nearest')
    plt.axis('off')
    plt.title(f"Mandelbrot set for a threshold of {threshold} and max iterations for divergence of {max_iterations}")
    plt.show()
