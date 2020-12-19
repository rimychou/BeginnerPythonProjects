def factorial(factor: int):
    """
    Using the factor `int` to calculate the factorial value
    """
    factorial_total = 1
    for value in range(factor):
        factorial_total += factorial_total * value
    return factorial_total


for values in range(36):
    print(values, factorial(values))
