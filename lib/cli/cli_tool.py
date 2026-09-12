import argparse

from lib.auth import authenticated

from .auth_cli import AuthCli
from .sales_cli import SalesCli
from .wine_cli import WineCli


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
    # create user
    auth_cli.create_user()

    # Wine batch management
    wine_cli = WineCli(subparser=subparser)
    # add wine
    wine_cli.add_wine()
    # view wine
    wine_cli.view_wine()
    # delete wine
    wine_cli.delete_wine()

    # sales reports
    sales_cli = SalesCli(subparser=subparser)
    # add sale
    sales_cli.add_sale()
    # sales report
    sales_cli.sales_report()

    # demo parser
    demo_parser = subparser.add_parser("demo", help="Testing authentication")
    demo_parser.add_argument("--any", help="testing any argument")
    demo_parser.set_defaults(func=demo_op)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
