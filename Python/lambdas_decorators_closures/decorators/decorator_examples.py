import functools
import time


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

        return result + '!'

    return wrapper


@upper
@add_exclamation_mark
def text(message):
    """This is text message"""
    return message


print(text('Hello World'))
print(f'Original function name is: {text.__name__}')
print(f'Original function documentation is: {text.__doc__}')


# Exam 2 - logging
def logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('-' * 50)
        print(f'Calling `{func.__name__}` function')
        result = func(*args, **kwargs)
        print(f'Result is: {result}')

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
        print('-' * 50)
        print(f'Calling `{func.__name__}` function')
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Time taken: {end - start:.2f}s.')

        return result

    return wrapper


@timing
def add(a, b):
    """This is add two numbers"""
    return a + b


add(1, 2)

# Exam 3 - Authorization
print('-' * 50)

user_database = {
    'user1': {'username': 'user1', 'role': 'admin'},
    'user2': {'username': 'user2', 'role': 'user'},
}


def get_username(username):
    return user_database.get(username)


def authorization(*roles):
    def authorization_decorator(func):

        @functools.wraps(func)
        def wrapper(username, *args, **kwargs):
            user = get_username(username)

            if user and user.get('role') in roles:
                return func(username, *args, **kwargs)
            else:
                return 'Not authorized'

        return wrapper

    return authorization_decorator


@authorization('admin')
def admin_dashboard(username):
    return f'Hello {username}! You are an admin!'


@authorization('admin', 'user')
def user_dashboard(username):
    return f'Hello {username}! You can access your user dashboard!'


print(admin_dashboard('user1'))
print(user_dashboard('user2'))

print(admin_dashboard('user2'))
print(user_dashboard('user1'))
