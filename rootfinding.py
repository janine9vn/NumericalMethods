import sympy
from typing import Tuple

x = sympy.symbols('x')


def bisection_root_finder(eqn: sympy.Basic, low: float, high: float, tolerance: float) -> Tuple[float, int, float]:
    """
    Given a single-variable sympy equation with x as the defined symbol, the low end of an interval, the high end of the interval,
    and the tolerance, it will calculate the root contained in the interval using the bisection method.
    It returns a tuple containing the root and the iterations taken

    If it takes more than 100 iterations, it breaks and returns early
    """
    root = 0

    if eqn.evalf(subs={x: root}) == 0:
        return root
    low_answer = eqn.evalf(subs={x: low})
    high_answer = eqn.evalf(subs={x: high})

    root = (low + high)/2
    iterations = 0

    while high-low > tolerance:
        low_answer = eqn.evalf(subs={x: low})
        high_answer = eqn.evalf(subs={x: high})

        if low_answer*high_answer >= 0:  # They're both on the same side of the axis, this is an issue
            return None
        else:
            mid = (low+high)/2
            root = mid
            if high_answer * eqn.evalf(subs={x: mid}) >= 0:
                high = mid
            else:
                low = mid
        iterations += 1
        if iterations > 100:
            break
    return root, iterations


def newton_raphson_root_finder(equation: sympy.Basic, first_guess: float, tolerance: float) -> Tuple[float, int]:
    """
    Given a single-variable sympy equation with x as the defined symbol, an initial guess, and a tolerance,
    this function will return a tuple containing the root and the iterations taken to find the root.
    It uses the Newton-Raphson method to find the root.
    """
    error = 1_000  # Starting with a high initial error
    x_o = first_guess
    f = equation
    f_prime = sympy.diff(equation, x)
    iterations = 0
    while error > tolerance:
        root = x_o - f.evalf(subs={x: x_o}, chop=True) / f_prime.evalf(subs={x: x_o}, chop=True)
        error = abs(root - x_o)
        x_o = root
        iterations += 1
    return root, iterations


def secant_root_finder(eqn: sympy.Basic, x0: float, x1: float, tolerance: float) -> Tuple[float, int]:
    """
    Given a sympy equation with x as the symbol, two initial guesses on the x-axis and a tolerance,
    It will find the root using the secant method

    Returns tuple containing root, number of iterations taken
    """
    error = 1_000  # High initial error
    iterations = 0

    while error > tolerance:
        # Calculating slope of the line between the two points
        slope = (eqn.evalf(subs={x: x1}) - eqn.evalf(subs={x: x0})) / (x1 - x0)

        # Calculating the next point
        root = x0 - ((eqn.evalf(subs={x: x0}))/slope)

        # Prep for next iteration
        error = abs(x0 - root)
        x0 = x1
        x1 = root
        iterations += 1
    return root, iterations
