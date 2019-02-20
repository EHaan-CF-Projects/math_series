"""
Overview of Module
"""


def fibonacci(n):
    """
    Overview of fibonacci
    """
    prev = 1
    current_fib = 1
    if n <= 2:
        print(current_fib)
    else:
        for i in range(n-2):
            prev, current_fib = current_fib, (prev + current_fib)
    return(current_fib)


def lucas(n):
    """
    overview of lucas
    """
    prev = 2
    current_lucas = 1

    if n < 2:
        return(prev)
    elif n == 2:
        return(current_lucas)
    elif n > 2:
        for i in range(n-2):
            prev, current_lucas = current_lucas, (prev + current_lucas)

    return(current_lucas)
