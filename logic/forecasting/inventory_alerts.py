class InventoryAlerts:
    """
    Inventory monitoring and low stock warnings.
    """

    LOW_STOCK_THRESHOLD = 50

    @classmethod
    def check_wine_batches(
        cls,
        wine_batches
    ):
        alerts = []

        for batch in wine_batches:

            if batch.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low wine stock: "
                    f"{batch.record_type.title()} "
                    f"({batch.quantity} bottles)"
                )

        return alerts

    @classmethod
    def check_grape_stock(
        cls,
        grape_stocks
    ):
        alerts = []

        for stock in grape_stocks:

            if stock.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low grape stock: "
                    f"{stock.category.title()} "
                    f"({stock.quantity} kg)"
                )

        return alerts

    @classmethod
    def generate_alerts(
        cls,
        wine_batches,
        grape_stocks
    ):
        return (
            cls.check_wine_batches(
                wine_batches
            ) +
            cls.check_grape_stock(
                grape_stocks
            )
        )