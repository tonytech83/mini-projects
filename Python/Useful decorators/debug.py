from functools import wraps


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@debug
def add(x, y):
    """Returns the sum of x and y"""
    return x + y


@debug
def greet(name, message="Hello"):
    """Returns a greeting message with the name"""
    return f"{message}, {name}!"


print(add(2, 3))
print(greet("Alice"))
print(greet("Bob", message="Hi"))
