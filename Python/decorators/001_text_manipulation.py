# Exam 1
def upper(func):
    @functools.wraps(func)  # stores the original function metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def add_exclamation_mark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result + "!"

    return wrapper


@upper
@add_exclamation_mark
def text(message):
    """This is text message"""
    return message


print(text("Hello World"))
print(f"Original function name is: {text.__name__}")
print(f"Original function documentation is: {text.__doc__}")
