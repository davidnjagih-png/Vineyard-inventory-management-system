from logic.forecasting.sales_projection import (
    SalesProjection
)


class Recommendations:
    """
    Inventory and sales recommendations.
    """

    @staticmethod
    def inventory_recommendation(
        current_stock,
        projected_sales
    ):
        """
        Compare inventory against projected demand.
        """

        if current_stock <= projected_sales:
            return (
                "Increase production or restock inventory."
            )

        return (
            "Current inventory levels are sufficient."
        )

    @staticmethod
    def sales_recommendation(records):
        """
        Recommend where to focus sales efforts.
        """

        top_category = (
            SalesProjection.top_selling_category(
                records
            )
        )

        if not top_category:
            return (
                "Not enough sales data available."
            )

        return (
            f"Focus marketing efforts on "
            f"{top_category.title()} products."
        )

    @staticmethod
    def seasonal_recommendation(
        season
    ):
        """
        Basic seasonal recommendations.
        """

        season = season.lower()

        recommendations = {
            "peak":
            "Increase stock levels before peak demand.",

            "normal":
            "Maintain regular inventory levels.",

            "low":
            "Reduce production to avoid excess stock."
        }

        return recommendations.get(
            season,
            "Season information unavailable."
        )