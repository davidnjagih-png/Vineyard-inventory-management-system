from logic.forecasting.sales_projection import (
    SalesProjection
)


class Recommendations:
    """
    Provides business recommendations.
    """

    @staticmethod
    def sales_recommendation(records):

        top_product = (
            SalesProjection.top_selling_product(
                records
            )
        )

        if top_product:

            return (
                f"Focus marketing efforts on "
                f"{top_product}."
            )

        return (
            "No sales data available."
        )

    @staticmethod
    def inventory_recommendation(
        current_stock,
        projected_sales
    ):

        if current_stock <= projected_sales:

            return (
                "Increase production or restock inventory."
            )

        return (
            "Inventory levels are sufficient."
        )

    @staticmethod
    def seasonal_recommendation(
        season
    ):

        season = season.lower()

        if season == "peak":

            return (
                "Increase inventory before peak demand."
            )

        if season == "low":

            return (
                "Reduce production to prevent surplus stock."
            )

        return (
            "Maintain current stock levels."
        )