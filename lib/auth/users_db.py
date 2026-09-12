import json
import os


def create_user(user):
    new_user = {"username": user.username, "role": user.role, "password": user.password}
    if os.path.exists("users_db.json") and os.path.getsize("users_db.json") > 0:
        with open("users_db.json", "r") as file:
            data = json.load(file)
    else:
        data = []

    data.append(new_user)

    with open("users_db.json", "w") as file:
        json.dump(data, file, indent=4)


def get_user(username, password):
    if os.path.exists("users_db.json") and os.path.getsize("users_db.json") > 0:
        with open("users_db.json", "r") as file:
            data = json.load(file)
        return next(
            user
            for user in data
            if user["username"] == username and user["password"] == password
        )
    else:
        return None
