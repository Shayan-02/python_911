def sums(a: int, b: int) -> int:
    """
    Returns the sum of a and b.

    :param a: The first number to add.
    :param b: The second number to add.
    :return: The sum of a and b.
    """
    y = a + b
    return y


print(sums(1, 2))


def f(x: int, y: int, z: int) -> int:
    """
    Returns a value computed from x, y, and z.
    The value is given by the formula 2*x^y + 3*z + 3.

    Parameters:
    
    x (int)
      The base of the exponentiation.
    y (int)
      The exponent.
    z (int)
      The value to add.
    
    Returns:
    a (int)
      The value computed from x, y, and z.
    """
    a = 2 * x**y + 3 * z + 3
    return a


print(f(1, 2, 3))
