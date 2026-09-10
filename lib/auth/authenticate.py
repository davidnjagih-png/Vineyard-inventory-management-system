from functools import wraps

from .save_user_session import get_user_session


def authenticated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        is_logged_in = get_user_session()
        if not is_logged_in:
            print("You need to be loged in to perform this operation.")
            return

        print(f"Logged in as {is_logged_in['username']}")
        result = func(*args, **kwargs)

        return result

    return wrapper
