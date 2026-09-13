from lib.auth import authenticated
from lib.inventory import Inventory


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
        view_wines_parser_group.add_argument(
            "--vintage", "--v", help="Filter by vintage"
        )

        view_wines_parser.add_argument(
            "--type", "--t", choices=["red", "white", "rose"], help="Filter by type"
        )

        view_wines_parser.set_defaults(func=WineCli.handle_view_wine)
        # Delete Wine

    def delete_wine(self):
        delete_wine_parser = self.subparser.add_parser(
            "delete-wine", help="Delete wines by category (vintage type quantity/all)"
        )
        delete_wine_parser.set_defaults(func=WineCli.handle_delete_wine)

    @staticmethod
    @authenticated(role="manager")
    def handle_add_wine(args):
        """Use args (type,vintage,quantity to add or update wines)"""
        inventory = Inventory()
        try:
            inventory.add_wine_batch(
                batch_id=args.type + args.vintage,
                wine_type=args.type,
                vintage=args.vintage,
                quantity=args.quantity,
            )
        except ValueError as e:
            print(e)

    @staticmethod
    @authenticated(role=["manager", "sales_team"])
    def handle_view_wine(args):
        """Use args to display wines, filter using vintage arg, or show all"""
        inventory = Inventory()
        if args.vintage and args.type:
            wine = next(
                (
                    wine
                    for wine in inventory._wine_batches
                    if wine.batch_id == args.type + args.vintage
                ),
                None,
            )
            if wine:
                print(
                    f"Inventory details for the {wine.vintage} vintage {wine.wine_type}: Quantity: {wine.quantity}"
                )
            else:
                print(f"We could not find the {args.vintage} vintage {args.type}")
            return
        elif args.vintage:
            wines = [
                wine for wine in inventory._wine_batches if wine.vintage == args.vintage
            ]
            if wines:
                for wine in wines:
                    print(
                        f"The {wine.vintage} vintage {wine.wine_type} has {wine.quantity} bottles."
                    )
            else:
                print(f"The {args.vintage} vintage is unavailable.")
            return
        elif args.type:
            wines = [
                wine for wine in inventory._wine_batches if wine.wine_type == args.type
            ]
            if wines:
                for wine in wines:
                    print(
                        f"The {wine.wine_type} {wine.vintage} vintage has {wine.quantity} bottles."
                    )
            else:
                print(f"There are no {args.type} wines available.")
            return
        else:
            wines = [wine for wine in inventory._wine_batches]
            if wines:
                for wine in wines:
                    print(
                        f"The {wine.wine_type} {wine.vintage} vintage has {wine.quantity} bottles."
                    )
            else:
                print("There are no wines available.")
            return

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
