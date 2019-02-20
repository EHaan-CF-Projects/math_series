"""
Overview of Module
"""


def fibonacci(n):
    """
    Overview of fibonacci
    """
    prev = 0
    current_fib = 1
    if n == (prev + 1):
        return(prev)
    else:
        for i in range(n - current_fib):
            prev, current_fib = current_fib, (prev + current_fib)
    return(current_fib)


def lucas(n):
    """
    overview of lucas
    """
    prev = 2
    current_lucas = 1

    if (n + 1) == prev:
        return(prev)
    else:
        for i in range(n - prev):
            prev, current_lucas = current_lucas, (prev + current_lucas)

    return(current_lucas)


# def sum_series(n, option1=0, option2=1):
#     """
#     overview of sum_series
#     """
#     
#     return(current_val)
