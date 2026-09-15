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

    def sales_recomendation(self):
        rec_parser = self.subparser.add_parser(
            "sales-rec", help="Get a recommendation based on sales data."
        )
        rec_parser.add_argument(
            "--seasonal",
            "--s",
            choices=["peak", "low"],
            help="Get seasonal recommendation",
        )
        rec_parser.set_defaults(func=SalesCli.handle_recommendation)

    @staticmethod
    @authenticated(role="sales_team")
    def handle_add_sale(args):
        """Add sale to record"""
        new_sale = SalesRecord(
            item=args.item, quantity=args.quantity, price_per_unit=args.price
        )
        create_sales(new_sale)

    @staticmethod
    @authenticated(role=["manager", "sales_team", "owner"])
    def handle_sales_report(args):
        """Display sales report"""
        records = SalesCli.get_sales_records()
        if records:
            report = ForecastingService.sales_report(records=records)
            message = f"""\n+------------------------------------------\n| Total Revenue: {report["total_revenue"]}\n+------------------------------------------\n| Wine Revenue: {report["wine_revenue"]}\n+------------------------------------------\n| Grape Revenue: {report["grape_revenue"]}\n+------------------------------------------\n| Top selling: {report["top_selling_product"]}
            """
            print(message)
        else:
            print("Nothing in the sales records")

    @staticmethod
    @authenticated(role=["manager", "sales_team", "owner"])
    def handle_recommendation(args):
        """Generate recommendation message based on sales record data"""
        if args.seasonal:
            print(ForecastingService.seasonal_recommendation(args.seasonal))

        records = SalesCli.get_sales_records()
        if records:
            print(ForecastingService.sales_recommendation(records=records))
        else:
            print("Nothing in the sales records.")

    @staticmethod
    def get_sales_records():
        """retune list of sales record instances"""
        records = get_all_sales()
        sales = [
            SalesRecord(
                item=record["item"],
                quantity=record["quantity"],
                price_per_unit=record["price_per_unit"],
            )
            for record in records
        ]
        return sales
