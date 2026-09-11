import getpass

from lib.auth import (
    authenticated,
    delete_user_session,
    save_user_session,
    create_user,
    get_user,
)
from lib.users import Admin, Manager, Owner, SalesTeam

"""
Todo: persist state in file when login confirmed and create decorator to authenticate other processes if user id logged in.
"""


class AuthCli:
    def __init__(self, subparser):
        self.subparser = subparser

    # login
    def login(self):
        login_parser = self.subparser.add_parser(
            "login", help="Login to application providing a username"
        )
        login_parser.add_argument("username", help="Enter the account username.")
        login_parser.add_argument(
            "password", nargs="?", default=None, help="Enter the account password"
        )
        login_parser.set_defaults(func=AuthCli.handle_login)

    # logout
    def logout(self):

        logout_parser = self.subparser.add_parser(
            "logout", help="Logout of the application"
        )
        logout_parser.set_defaults(func=AuthCli.handle_logout)

    def create_user(self):
        create_user_parser = self.subparser.add_parser(
            "new-user", help="Create new User"
        )
        create_user_parser.add_argument("username", help="New User username")
        create_user_parser.add_argument("password", help="New User password")
        create_user_parser.add_argument(
            "role",
            choices=["admin", "manager", "owner", "sales_team"],
            help="New User role",
        )
        create_user_parser.set_defaults(func=AuthCli.handle_create_user)

    @staticmethod
    def handle_login(args):
        """Login user and store creds in file"""
        print("Username: ", args.username)

        if args.password is None:
            password = getpass.getpass(prompt=f"Password for {args.username}:")
            print("password: ", password)
        else:
            password = args.password
        # Todo: validate user exists in user json file before creating session
        # login user by saving session
        user = get_user(args.username, password=password)
        if user:
            print(f"Welcome back {user}")
            save_user_session(user)

        else:
            print("That user does not exist bud.")

    @staticmethod
    @authenticated
    def handle_logout(args):
        """Delete user session on user logout"""
        delete_user_session()

    @staticmethod
    @authenticated(role="admin")
    def handle_create_user(args):
        """Create new user if user is admin"""
        if args.role == "admin":
            new_user = Admin(username=args.username, password=args.password)
        elif args.role == "manager":
            new_user = Manager(username=args.username, password=args.password)
        elif args.role == "owner":
            new_user = Owner(username=args.username, password=args.password)
        elif args.role == "sales_team":
            new_user = SalesTeam(username=args.username, password=args.password)

        create_user(new_user)
