import argparse

from lib.auth import authenticated

from .auth_cli import AuthCli


@authenticated
def demo_op(args):
    print(f"You will see this if you have loggin. Arg passed:{args.any}")


def main():
    parser = argparse.ArgumentParser(
        prog="Vineyard Inventory Management",
        description="A vineyard inventory management CLI tool",
    )
    subparser = parser.add_subparsers()

    # Authentication
    auth_cli = AuthCli(subparser=subparser)
    # login
    auth_cli.login()
    # logout
    auth_cli.logout()
    # Wine batch management
    """
    todo: Add new wine (@params: type[red,white,rose], vintage, quantity) , Edit wine, Delete, View wines. (Sales 'r',Owner 'r', Admin 'r,w' ) 
    """
    # add wine
    add_wine_parser = subparser.add_parser(
        "wines", help="Add, Edit, Delete, View wines"
    )

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
