from typing import Union, Sequence

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spinter

Num = Union[int, float]


def piecewise_linear(x_data: Sequence[Num], y_data: Sequence[Num], x_to_find: Num) -> float:
    """
    Shows plot for piece-wise linear with given data and the estimated y-value for the given x value.
    Prints the lowest y-value and its corresponding x-value.
    Will also interpolate and return the y-value for a given x-value.
    """

    plt.plot(x_data, y_data)

    # This does the piece wise interopolation
    for i, x in enumerate(x_data):
        if x_data[i] <= x_to_find < x_data[i+1]:
            y_found = y_data[i] + (y_data[i+1] - y_data[i])/(x_data[i+1] - x_data[i])*(x_to_find - x_data[i])

    plt.plot(x_to_find, y_found, 'r+')
    plt.title("Piece-Wise Interpolation")
    plt.show()

    print(f"Minimum y-value: {min(y_data)}")
    print(f"Corresponding x-value: {x_data[y_data.index(min(y_data))]}")

    return y_found


def exact_data_fit_polynomial(x_data: Sequence[Num], y_data: Sequence[Num], x_to_find: Num, polynomial_order: int) -> Union[float, None]:
    """
    Given: x_data, y_data, and x-value to interpolate, and the polynomial order
    this function will print the coefficients for the specified order interpolation polynomial.
    Polynomial will fit all data points and return the interpolated y-value from the given x-value.
    It will print the minimum y-value and the corresponding x-value for the interpolation function.

    This function returns the interpolated y-value from the given x-value.

    The polynomial order (rank) must be square with the data, otherwise a value of None will be returned.
    """
    if len(x_data) != polynomial_order + 1:  # Checking if the rank is square and we can get an exact solution
        return None

    plt.plot(x_data, y_data, 'r+')

    # We create the polynomial array we need to solve to get the coefficients array
    a_array = []
    for x in x_data:
        inner_temp_array = []
        for exponent in range(polynomial_order+1):
            inner_temp_array.append(x**exponent)
        a_array.append(inner_temp_array)

    coefficients = np.linalg.solve(a_array, y_data)
    print(f"Coefficients: {coefficients}")

    # Doing the interpolation
    y_found = 0
    for i, coeff in enumerate(coefficients):
        y_found += coeff*x_to_find**i

    # It's time for some plotting!
    x_vals = np.linspace(-1, 1, 1000)
    y_vals = []
    for x in x_vals:
        y_temp = 0
        for i, coeff in enumerate(coefficients):
            y_temp += coeff*x**i
        y_vals.append(y_temp)
    plt.plot(x_vals, y_vals)
    plt.plot(x_to_find, y_found, 'g*')
    plt.title(f"{polynomial_order}-Order Polynomial Interpolation Passing Through All Data Points")
    plt.show()

    # Finding the lowest y-value min using a fine grid mesh
    y_min = min(y_vals)
    x_min = x_vals[y_vals.index(min(y_vals))]
    print(f"Minimum y-value found was: {y_min}, corresponding x-value was: {x_min}")

    return y_found


def least_squares_polynomial(x_data: Sequence[Num], y_data: Sequence[Num], x_to_find: Num, polynomial_order: int) -> float:
    """
    Given x-data, y-data, an x-value to interpolate, and a polynomial solution order
    this function will find the least-squares polynomial solution
    and return the interpolated y-value for the given x-value.

    It will print the coefficients for the resulting polynomial.
    It will provide a plot of the polynomial, with the original data points, and the interpolated value.
    Additionally it will print the lowest y-value and its corresponding x-value.
    """
    plt.plot(x_data, y_data, 'r+')

    # Solving for the polynomial coefficients
    a_array = []
    for x in x_data:
        inner_temp_array = []
        for exponent in range(polynomial_order+1):
            inner_temp_array.append(x**exponent)
        a_array.append(inner_temp_array)
    a_array = np.array(a_array)
    a_array_trans = np.matrix.transpose(a_array)
    coefficients = np.linalg.solve(a_array_trans.dot(a_array), a_array_trans.dot(y_data))
    print(f"Coefficients: {coefficients}")

    # Let's find the interpolated y-value
    y_found = 0
    for i, coeff in enumerate(coefficients):
        y_found += coeff*x_to_find**i
    print(y_found)

    # Iterating through the polynomial to provide a plot
    x_vals = np.linspace(-1, 1, 1000)
    y_vals = []
    for x in x_vals:
        y_temp = 0
        for i, coeff in enumerate(coefficients):
            y_temp += coeff*x**i
        y_vals.append(y_temp)
    plt.plot(x_vals, y_vals)
    plt.plot(x_to_find, y_found, 'g*')
    plt.title(f"Least-Squares {polynomial_order}-Order Polynomial Interpolation")
    plt.show()

    # Printing y_min and corresponding x_min
    y_min = min(y_vals)
    x_min = x_vals[y_vals.index(min(y_vals))]
    print(f"Minimum y-value found was: {y_min}, corresponding x-value was: {x_min}")

    return y_found


def cubic_spline(x_data: Sequence[Num], y_data: Sequence[Num], x_to_find: Num) -> float:
    """
    Given x_data, y_data, and an x-value to find, this function will return the
    corresponding y-value using SciPy's cubic spline interpolation.
    It will display a graph showing the data points, interpolation, and the interpolated value.
    It will also print the minimum y-value for the interpolation and its corresponding x-value.
    """
    plt.plot(x_data, y_data)
    x_vals = np.linspace(-1, 1, 1000)
    y_vals = []

    cs = spinter.CubicSpline(x_data, y_data)
    for x in x_vals:
        y_vals.append(cs(x))
    plt.plot(x_vals, y_vals)

    # Let's find the interpolated data point
    y_found = cs(x_to_find)
    plt.plot(x_to_find, y_found, 'g*')
    plt.title("Cubic Spline Interpolation")
    plt.show()

    y_min = min(y_vals)
    x_min = x_vals[y_vals.index(min(y_vals))]
    print(f"Minimum y-value found was: {y_min}, corresponding x-value was: {x_min}")

    return y_found
