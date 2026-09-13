from lib.auth import authenticated
from lib.inventory import Inventory


class GrapeCli:
    def __init__(self, subparser):
        self.subparser = subparser

        """
    todo: Add new grape (@params: type[table,wine], variety, quantity) , Edit grape, Delete, View grapes. (Sales 'r',Owner 'r', Admin 'r,w' ) 
    """

    # add grape
    def add_grape(self):
        add_grape_parser = self.subparser.add_parser(
            "add-grape", help="Add grape - type, variety, quantity"
        )
        add_grape_parser.add_argument(
            "type", choices=["table", "wine"], help="grape type table or wine"
        )
        add_grape_parser.add_argument(
            "variety",
            choices=["red", "white", "rose"],
            help="The grape variety e.g red",
        )
        add_grape_parser.add_argument("quantity", type=int, help="kilogram quantity")
        add_grape_parser.set_defaults(func=GrapeCli.handle_add_grape)

        # View grapes

    def view_grape(self):
        view_grapes_parser = self.subparser.add_parser(
            "view-grapes",
            help="Display grapes - '--all (default) --variety (filter by variety)",
        )
        view_grapes_parser_group = view_grapes_parser.add_argument_group(
            "Display Filter", "Display all grapes or filte by variety"
        ).add_mutually_exclusive_group()
        view_grapes_parser_group.add_argument(
            "--all",
            nargs="?",
            const=True,
            required=False,
            help="Display all grapes",
        )
        view_grapes_parser_group.add_argument(
            "--variety",
            "--v",
            choices=["red", "white", "rose"],
            help="Filter by variety",
        )

        view_grapes_parser.add_argument(
            "--type", "--t", choices=["table", "wine"], help="Filter by type"
        )

        view_grapes_parser.set_defaults(func=GrapeCli.handle_view_grape)
        # Delete grape

    def delete_grape(self):
        delete_grape_parser = self.subparser.add_parser(
            "delete-grape", help="Delete grapes by category (variety type quantity/all)"
        )
        delete_grape_parser.set_defaults(func=GrapeCli.handle_delete_grape)

    @staticmethod
    @authenticated(role="manager")
    def handle_add_grape(args):
        """Use args (type,variety,quantity to add or update grapes)"""
        inventory = Inventory()
        try:
            inventory.add_grape_stock(
                grape_type=args.type,
                variety=args.variety,
                quantity=args.quantity,
            )
        except ValueError as e:
            print(e)

    @staticmethod
    @authenticated(role=["manager", "sales_team"])
    def handle_view_grape(args):
        """Use args to display grapes, filter using variety arg, or show all"""
        inventory = Inventory()
        if args.variety and args.type:
            grape = next(
                (
                    grape
                    for grape in inventory._grape_stock
                    if grape.grape_type == args.type and args.variety == grape.variety
                ),
                None,
            )
            if grape:
                print(
                    f"Inventory details for the {grape.variety} variety {grape.grape_type}: Quantity: {grape.quantity}"
                )
            else:
                print(
                    f"We could not find the {args.variety} variety in {args.type} grapes"
                )
            return
        elif args.variety:
            grapes = [
                grape
                for grape in inventory._grape_stock
                if grape.variety == args.variety
            ]
            if grapes:
                for grape in grapes:
                    print(
                        f"The {grape.variety} variety {grape.grape_type} has {grape.quantity}."
                    )
            else:
                print(f"The {args.variety} variety is unavailable.")
            return
        elif args.type:
            grapes = [
                grape
                for grape in inventory._grape_stock
                if grape.grape_type == args.type
            ]
            if grapes:
                for grape in grapes:
                    print(
                        f"The {grape.grape_type} {grape.variety} variety has {grape.quantity}."
                    )
            else:
                print(f"There are no {args.type} grapes available.")
            return
        else:
            grapes = [grape for grape in inventory._grape_stock]
            if grapes:
                for grape in grapes:
                    print(
                        f"The {grape.grape_type} {grape.variety} variety has {grape.quantity}."
                    )
            else:
                print("There are no grapes available.")
            return

    # todo: remove specific quantity
    @staticmethod
    @authenticated(role="manager")
    def handle_delete_grape(args):
        variety = input("PLease specify a variety: ")
        type = input("Please specify a type [all, red, white, rose]: ")
        verify = input(
            f"Are you sure you want to delete {type} from {variety} (Yes / No) ?"
        )
        inventory = Inventory()
        try:
            if verify.lower() == "yes":
                if type == "all":
                    grapes = [
                        grape
                        for grape in inventory._grape_batches
                        if grape.variety == variety
                    ]
                    for item in grapes:
                        inventory.delete_grape_batch(item.batch_id)
                else:
                    inventory.remove_grape_stock(
                        type,
                    )
            else:
                print("Operation discarded")
        except ValueError as e:
            print(e)
