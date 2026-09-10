import argparse

from lib.auth import authenticated

from .auth_cli import AuthCli


@authenticated
def demo_op(args):
    print(f"You will see this if you have loggin. Arg passed:{args.any}")


@authenticated
def handle_add_wine(args):
    """Use args (type,vintage,quantity to add or update wines)"""
    print(args)


def handle_view_wine(args):
    """Use args to display wines, filter using vintage arg, or show all"""
    print(args)


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
        "add-wine", help="Add wine - type, vintage, quantity"
    )
    add_wine_parser.add_argument(
        "type", choices=["red", "white", "rose"], help="Wine type"
    )
    add_wine_parser.add_argument("vintage", help="The wine vintage e.g 2001")
    add_wine_parser.add_argument("quantity", type=int, help="Bottle quantity")
    add_wine_parser.set_defaults(func=handle_add_wine)
    # View Wines
    view_wines_parser = subparser.add_parser(
        "view-wines",
        help="Display wines - '--all (default) --vintage (filter by vintage)",
    )
    view_wines_parser_group = view_wines_parser.add_argument_group(
        "Display Filter", "Display all wines or filte by vintage"
    ).add_mutually_exclusive_group()
    view_wines_parser_group.add_argument(
        "--all",
        nargs="?",
        const=True,
        required=False,
        help="Display all wines",
    )
    view_wines_parser_group.add_argument("--vintage", help="Filter by vintage")

    view_wines_parser.set_defaults(func=handle_view_wine)

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
