from logic.forecasting.wine_forecast import WineForecast
from logic.forecasting.grape_forecast import GrapeForecast
from logic.forecasting.sales_projection import SalesProjection
from logic.forecasting.inventory_alerts import InventoryAlerts
from logic.forecasting.recommendations import Recommendations


class ForecastingService:
    """
    Main service used by the CLI.
    """

    @staticmethod
    def wine_projection(
        wine_type,
        grape_quantity
    ):
        return WineForecast.generate_forecast(
            wine_type,
            grape_quantity
        )

    @staticmethod
    def table_grape_projection(
        quantity_kg
    ):
        return GrapeForecast.generate_forecast(
            quantity_kg
        )

    @staticmethod
    def sales_report(records):

        return SalesProjection.generate_report(
            records
        )

    @staticmethod
    def inventory_alerts(
        wine_batches,
        grape_stocks
    ):

        return (
            InventoryAlerts.check_wine_stock(
                wine_batches
            )
            +
            InventoryAlerts.check_grape_stock(
                grape_stocks
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