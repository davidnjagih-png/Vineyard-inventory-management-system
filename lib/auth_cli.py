import getpass

from lib.auth import authenticated, delete_user_session, save_user_session

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

    @staticmethod
    def handle_login(args):
        """Login user and store creds in file"""
        print("Username: ", args.username)

        if args.password is None:
            password = getpass.getpass(prompt=f"Password for {args.username}:")
            print("password: ", password)
        # Todo: validate user exists in user json file before creating session
        # login user by saving session
        save_user_session(args.username)

    @staticmethod
    @authenticated
    def handle_logout(args):
        """Delete user session on user logout"""
        delete_user_session()
