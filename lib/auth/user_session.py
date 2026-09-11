import json


def save_user_session(user):
    with open("user_session.json", "w") as file:
        json.dump(user, file, indent=4)
    print(f"Logged in as {user['username']}")


def get_user_session():
    try:
        with open("user_session.json", "r") as file:
            data = json.load(file)
        return data or {}
    except FileNotFoundError:
        return {}


def delete_user_session():
    with open("user_session.json", "w") as file:
        json.dump({}, file, indent=4)
    print("Logged out.")
