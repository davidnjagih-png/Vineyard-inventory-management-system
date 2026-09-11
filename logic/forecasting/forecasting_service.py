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
    Main forecasting entry point.
    Used by CLI and main.py
    """

    @staticmethod
    def sales_report(records):
        """
        Generate sales report.
        """
        return (
            SalesProjection.generate_report(
                records
            )
        )

    @staticmethod
    def inventory_report(
        wine_batches,
        grape_stocks
    ):
        """
        Generate inventory alert report.
        """
        return (
            InventoryAlerts.generate_alerts(
                wine_batches,
                grape_stocks
            )
        )

    @staticmethod
    def recommendation_report(
        records
    ):
        """
        Generate sales recommendation report.
        """
        return (
            Recommendations.sales_recommendation(
                records
            )
        )

    @staticmethod
    def stock_recommendation(
        current_stock,
        projected_sales
    ):
        """
        Generate inventory recommendation.
        """
        return (
            Recommendations.inventory_recommendation(
                current_stock,
                projected_sales
            )
        )