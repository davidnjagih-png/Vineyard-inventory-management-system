class InventoryAlerts:

    LOW_STOCK_THRESHOLD = 50

    @classmethod
    def wine_alerts(
        cls,
        wine_batches
    ):

        alerts = []

        for batch in wine_batches:

            if batch.quantity < cls.LOW_STOCK_THRESHOLD:

                alerts.append(
                    f"Low stock: "
                    f"{batch.record_type} wine "
                    f"({batch.quantity})"
                )

        return alerts

    @classmethod
    def grape_alerts(
        cls,
        grape_stocks
    ):

        alerts = []

        for stock in grape_stocks:

            if stock.quantity < cls.LOW_