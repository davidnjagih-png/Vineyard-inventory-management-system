from lib.auth import authenticated
from lib.sales_record import SalesRecord, create_sales, get_all_sales
from logic.forecasting import ForecastingService


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

    # sales report
    def sales_report(self):
        report_parser = self.subparser.add_parser(
            "sales-report", help="Get a summary of the sales"
        )
        report_parser.set_defaults(func=SalesCli.handle_sales_report)

    @staticmethod
    @authenticated(role="sales_team")
    def handle_add_sale(args):
        """Add sale to record"""
        new_sale = SalesRecord(
            item=args.item, quantity=args.quantity, price_per_unit=args.price
        )
        create_sales(new_sale)

    @staticmethod
    def handle_sales_report(args):
        """Display sales report"""
        records = get_all_sales()
        if not records:
            print("Nothing in the sales records.")
            return
        sales = [
            SalesRecord(
                item=record["item"],
                quantity=record["quantity"],
                price_per_unit=record["price_per_unit"],
            )
            for record in records
        ]

        report = ForecastingService.sales_report(sales)
        message = f"""\n+------------------------------------------\n| Total Revenue: {report["total_revenue"]}\n+------------------------------------------\n| Wine Revenue: {report["wine_revenue"]}\n+------------------------------------------\n| Grape Revenue: {report["grape_revenue"]}\n+------------------------------------------\n| Top selling: {report["top_selling_product"]}
        """
        print(message)
