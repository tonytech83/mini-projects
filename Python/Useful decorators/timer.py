import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start} seconds")
        return result

    return wrapper


@timer
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@timer
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(factorial(10))
print(fibonacci(10))
