f = open("./test.txt", mode="r+", encoding="utf-8")
f.write("salam")
print(f.read())


def sums(n1, n2):
    """
    Returns the sum of two numbers.

    Parameters:
    n1 (int or float): The first number.
    n2 (int or float): The second number.

    Returns:
    int or float: The sum of n1 and n2.
    """
    # Calculate the sum of the two numbers and return the result
    return n1 + n2
