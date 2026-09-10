class User:
    all = []

    def __init__(self, username, password):
        """Initialize object parameters"""

    @property
    def password(self):
        """return password value"""

    @password.setter
    def password(self, value):
        """validate password"""

    @classmethod
    def validate_user(cls, username, password):
        """Authenticate user by confirming existence in User.all with matching values"""

    @classmethod
    def add_user(cls, user):
        """Add user to class parameter all persistence"""
