import functools
import time


# Exam 2 - logging
def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 50)
        print(f"Calling `{func.__name__}` function")
        result = func(*args, **kwargs)
        print(f"Result is: {result}")

        return result

    return wrapper


@logging
def add(a, b):
    """This is add two numbers"""
    return a + b


add(1, 2)


def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 50)
        print(f"Calling `{func.__name__}` function")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.2f}s.")

        return result

    return wrapper


@timing
def add(a, b):
    """This is add two numbers"""
    return a + b


add(1, 2)
