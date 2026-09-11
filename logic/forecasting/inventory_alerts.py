class InventoryAlerts:
    """
    Generates low stock alerts.
    """

    LOW_STOCK_THRESHOLD = 50

    @classmethod
    def check_wine_stock(cls, wine_batches):

        alerts = []

        for batch in wine_batches:

            if batch.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low stock alert: "
                    f"{batch.record_type} wine "
                    f"({batch.quantity} remaining)"
                )

        return alerts

    @classmethod
    def check_grape_stock(cls, grape_stocks):

        alerts = []

        for stock in grape_stocks:

            if stock.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low stock alert: "
                    f"{stock.category} "
                    f"({stock.quantity} kg remaining)"
                )

        return alerts