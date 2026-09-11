from functools import wraps

from .user_session import get_user_session


def authenticated(role=None):
    def authenticator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            is_logged_in = get_user_session()
            if not is_logged_in:
                print("You need to be loged in to perform this operation.")
                return

            print(f"Logged in as {is_logged_in['username']}")
            if not role or role == is_logged_in["role"]:
                result = func(*args, **kwargs)
            else:
                print(f"You need to be an {role} to perform this operation.")
                return

            return result

        return wrapper

    return authenticator
