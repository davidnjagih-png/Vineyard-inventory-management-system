import argparse
import getpass

from lib.auth import authenticated, save_user_session

"""
Todo: persist state in file when login confirmed and create decorator to authenticate other processes if user id logged in.
"""


def handle_login(args):
    """Login user and store creds in file"""
    print("Username: ", args.username)

    if args.password is None:
        password = getpass.getpass(prompt=f"Password for {args.username}:")
        print("password: ", password)
    # Todo: validate user exists in user json file before creating session
    # login user by saving session
    save_user_session(args.username)


@authenticated
def demo_op(args):
    print(f"You will see this if you have loggin. Arg passed:{args.any}")


def main():
    parser = argparse.ArgumentParser(
        prog="Vineyard Inventory Management",
        description="A vineyard inventory management CLI tool",
    )
    subparser = parser.add_subparsers()

    # login
    login_parser = subparser.add_parser(
        "login", help="Login to application providing a username"
    )
    login_parser.add_argument("username", help="Enter the account username.")
    login_parser.add_argument(
        "password", nargs="?", default=None, help="Enter the account password"
    )
    login_parser.set_defaults(func=handle_login)

    # demo parser
    demo_parser = subparser.add_parser("demo", help="Testing authentication")
    demo_parser.add_argument("--any", help="testing any argument")
    demo_parser.set_defaults(func=demo_op)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

    print(args)
