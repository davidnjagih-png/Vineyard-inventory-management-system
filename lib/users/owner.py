from .user import User

class Owner(User):
    def __init__(self, username, password):
        super().__init__(username, password, "owner")