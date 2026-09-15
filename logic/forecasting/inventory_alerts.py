class InventoryAlerts:
    """
    Handles low stock monitoring.
    """

    LOW_STOCK_THRESHOLD = 50

    @classmethod
    def wine_stock_alerts(
        cls,
        wine_batches
    ):
        alerts = []

        for batch in wine_batches:

            if batch.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low wine stock: "
                    f"{batch.record_type} "
                    f"({batch.quantity} remaining)"
                )

        return alerts

    @classmethod
    def grape_stock_alerts(
        cls,
        grape_stock
    ):
        alerts = []

        for stock in grape_stock:

            if stock.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low grape stock: "
                    f"{stock.category} "
                    f"({stock.quantity} kg remaining)"
                )

        return alerts

    @classmethod
    def generate_alerts(
        cls,
        wine_batches,
        grape_stock
    ):
        return (
            cls.wine_stock_alerts(
                wine_batches
            )
            +
            cls.grape_stock_alerts(
                grape_stock
            )
        )