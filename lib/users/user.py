class User:
    all = []

    def __init__(self, username, password, role=None):
        self._username = username
        self.password = password
        self._role = role

        User.add_user(self)

    @property
    def username(self):
        return self._username

    @property
    def name(self):
        return self._username
    
    @property
    def role(self):
        return self._role


    @property
    def password(self):
        return self._password
    

    @password.setter
    def password(self, value):
        if not value:
            raise ValueError("password cannot be empty")
        
        self._password = value
    
    @classmethod
    def add_user(cls, user):
        cls.all.append(user)
    


    @classmethod
    def validate_user(cls, username, password):
        for user in cls.all:
            if user.username == username and user.password == password:
                return user
        
        raise ValueError("Invalid username or password")
    
    @classmethod
    def get_user(cls, username):
        for user in cls.all:
            if user.username == username:
                return user
        
        raise ValueError("user not found")

