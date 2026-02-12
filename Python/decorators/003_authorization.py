import functools

# Exam 3 - Authorization
print("-" * 50)

user_database = {
    "user1": {"username": "user1", "role": "admin"},
    "user2": {"username": "user2", "role": "user"},
}


def get_username(username):
    return user_database.get(username)


def authorization(*roles):
    def authorization_decorator(func):
        @functools.wraps(func)
        def wrapper(username, *args, **kwargs):
            user = get_username(username)

            if user and user.get("role") in roles:
                return func(username, *args, **kwargs)
            else:
                return "Not authorized"

        return wrapper

    return authorization_decorator


@authorization("admin")
def admin_dashboard(username):
    return f"Hello {username}! You are an admin!"


@authorization("admin", "user")
def user_dashboard(username):
    return f"Hello {username}! You can access your user dashboard!"


print(admin_dashboard("user1"))
print(user_dashboard("user2"))

print(admin_dashboard("user2"))
print(user_dashboard("user1"))
