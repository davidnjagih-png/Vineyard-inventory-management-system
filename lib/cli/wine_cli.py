from lib.auth import authenticated


class WineCli:
    def __init__(self, subparser):
        self.subparser = subparser

        """
    todo: Add new wine (@params: type[red,white,rose], vintage, quantity) , Edit wine, Delete, View wines. (Sales 'r',Owner 'r', Admin 'r,w' ) 
    """

    # add wine
    def add_wine(self):
        add_wine_parser = self.subparser.add_parser(
            "add-wine", help="Add wine - type, vintage, quantity"
        )
        add_wine_parser.add_argument(
            "type", choices=["red", "white", "rose"], help="Wine type"
        )
        add_wine_parser.add_argument("vintage", help="The wine vintage e.g 2001")
        add_wine_parser.add_argument("quantity", type=int, help="Bottle quantity")
        add_wine_parser.set_defaults(func=WineCli.handle_add_wine)

        # View Wines

    def view_wine(self):
        view_wines_parser = self.subparser.add_parser(
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

        view_wines_parser.add_argument(
            "--type", choices=["red", "white", "rose"], help="Filter by type"
        )

        view_wines_parser.set_defaults(func=WineCli.handle_view_wine)
        # Delete Wine

    def delete_wine(self):
        delete_wine_parser = self.subparser.add_parser(
            "delete-wine", help="Delete wines by category (vintage type quantity/all)"
        )
        delete_wine_parser.set_defaults(func=WineCli.handle_delete_wine)

    @staticmethod
    @authenticated
    def handle_add_wine(args):
        """Use args (type,vintage,quantity to add or update wines)"""
        print(args)

    @staticmethod
    @authenticated
    def handle_view_wine(args):
        """Use args to display wines, filter using vintage arg, or show all"""
        print(args)

    @staticmethod
    @authenticated
    def handle_delete_wine(args):
        vintage = input("PLease specify a vintage: ")
        type = input("PLease specify a type [all, red, white, rose]: ")
        verify = input(
            f"Are you sure you want to delete {type} from {vintage} (Yes / No) ?"
        )

        if verify.lower() == "yes":
            print("Deleted..")
