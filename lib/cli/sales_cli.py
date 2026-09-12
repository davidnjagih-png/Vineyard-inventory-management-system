from lib.auth import authenticated
from lib.sales_record import SalesRecord, create_sales


class SalesCli:
    def __init__(self, subparser):
        self.subparser = subparser

    # add sale
    def add_sale(self):
        """create new sales record"""
        add_sale_parser = self.subparser.add_parser("add-sale", help="Add sale record")
        add_sale_parser.add_argument(
            "item", choices=["wine", "grape"], help="item type. wine or grape"
        )
        add_sale_parser.add_argument(
            "quantity", type=int, help="Quantity of items sold"
        )
        add_sale_parser.add_argument(
            "price", type=float, help="Price per unit of items"
        )
        add_sale_parser.set_defaults(func=SalesCli.handle_add_sale)

    @staticmethod
    @authenticated(role="sales_team")
    def handle_add_sale(args):
        """Add sale to record"""
        new_sale = SalesRecord(
            item=args.item, quantity=args.quantity, price_per_unit=args.price
        )
        create_sales(new_sale)
