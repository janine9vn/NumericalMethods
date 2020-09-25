from typing import List, TypeVar

import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spinter

Num =  Union[int, float]

def piecewise_linear(x_data: Sequence[Num], y_data: Sequence[Num], x_to_find: float):
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
