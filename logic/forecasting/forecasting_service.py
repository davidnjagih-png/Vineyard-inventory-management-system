from logic.forecasting.sales_projection import (
    SalesProjection
)

from logic.forecasting.inventory_alerts import (
    InventoryAlerts
)

from logic.forecasting.recommendations import (
    Recommendations
)


class ForecastingService:
    """
    Main forecasting service.
    Used by CLI and main.py
    """

    @staticmethod
    def sales_report(records):

        return (
            SalesProjection.generate_report(
                records
            )
        )

    @staticmethod
    def inventory_report(
        wine_batches,
        grape_stock
    ):

        return (
            InventoryAlerts.generate_alerts(
                wine_batches,
                grape_stock
            )
        )

    @staticmethod
    def sales_recommendation(
        records
    ):

        return (
            Recommendations.sales_recommendation(
                records
            )
        )

    @staticmethod
    def inventory_recommendation(
        current_stock,
        projected_sales
    ):

        return (
            Recommendations.inventory_recommendation(
                current_stock,
                projected_sales
            )
        )

    @staticmethod
    def seasonal_recommendation(
        season
    ):

        return (
            Recommendations.seasonal_recommendation(
                season
            )
        )