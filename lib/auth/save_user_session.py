import json


def save_user_session(username):
    current_user = {
        "username": username,
    }
    with open("user_session.json", "w") as file:
        json.dump(current_user, file, indent=4)
    print(f"Logged in as {username}")


def get_user_session():
    with open("user_session.json", "r") as file:
        data = json.load(file)
    return data or {}
