class SalesProjection:
    """
    Analyze sales records and generate projections.
    """

    @staticmethod
    def total_revenue_projection(records):
        """
        Calculate projected revenue from all sales records.
        """
        return sum(
            record.calculate_projection()
            for record in records
        )

    @staticmethod
    def wine_revenue_projection(records):
        """
        Calculate projected revenue from wine only.
        """
        return sum(
            record.calculate_projection()
            for record in records
            if record.item_type.lower() == "wine"
        )

    @staticmethod
    def grape_revenue_projection(records):
        """
        Calculate projected revenue from table grapes only.
        """
        return sum(
            record.calculate_projection()
            for record in records
            if record.item_type.lower() == "table_grapes"
        )

    @staticmethod
    def revenue_by_category(records):
        """
        Revenue grouped by category.
        Example:
        red, white, rose, table_grapes
        """
        category_totals = {}

        for record in records:

            category = record.category.lower()

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += (
                record.calculate_projection()
            )

        return category_totals

    @staticmethod
    def top_selling_category(records):
        """
        Returns category with highest projected revenue.
        """

        category_totals = (
            SalesProjection.revenue_by_category(records)
        )

        if not category_totals:
            return None

        return max(
            category_totals,
            key=category_totals.get
        )

    @staticmethod
    def generate_report(records):
        """
        Generate complete sales report.
        """

        return {
            "total_revenue":
            SalesProjection.total_revenue_projection(
                records
            ),

            "wine_revenue":
            SalesProjection.wine_revenue_projection(
                records
            ),

            "grape_revenue":
            SalesProjection.grape_revenue_projection(
                records
            ),

            "revenue_by_category":
            SalesProjection.revenue_by_category(
                records
            ),

            "top_selling_category":
            SalesProjection.top_selling_category(
                records
            )
        }