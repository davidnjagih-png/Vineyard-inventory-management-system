from lib.sales_record.pricing import price_grapes, price_wine
from lib.sales_record.projections import calculate_projection
from lib.sales_record.reporting import generate_sales_report


class SalesRecord:
    def __init__(self, item, quantity, price_per_unit):
        self.item = item
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def calculate_projection(self):
        return calculate_projection(self.quantity, self.price_per_unit)

    def price_item(self):
        if "wine" in self.item.lower():
            return price_wine(self.item, self.quantity, self.price_per_unit)
        elif "grape" in self.item.lower():
            return price_grapes(self.quantity, self.price_per_unit)
        else:
            raise ValueError("Unknown item type")

    @staticmethod
    def report(records):
        return generate_sales_report(records)
