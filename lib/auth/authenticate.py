from functools import wraps

from .user_session import get_user_session


def authenticated(role=None):
    roles = [role] if isinstance(role, str) else role

    def authenticator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("auth called with role: ", role)

            is_logged_in = get_user_session()

            if not is_logged_in:
                print("You need to be loged in to perform this operation.")
                return

            if not role or is_logged_in["role"] in roles:
                result = func(*args, **kwargs)
            else:
                print(f"You need to be an {role} to perform this operation.")
                return

            return result

        return wrapper

    return authenticator
