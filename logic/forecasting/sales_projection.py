class SalesProjection:
    """
    Projection and report logic
    based on SalesRecord objects.
    """

    @staticmethod
    def total_revenue_projection(records):

        return sum(
            record.calculate_projection()
            for record in records
        )

    @staticmethod
    def revenue_by_category(records):

        projections = {}

        for record in records:

            category = record.category

            projections.setdefault(
                category,
                0
            )

            projections[category] += (
                record.calculate_projection()
            )

        return projections

    @staticmethod
    def top_selling_category(records):

        projections = (
            SalesProjection.revenue_by_category(
                records
            )
        )

        return max(
            projections,
            key=projections.get
        )

    @staticmethod
    def wine_projection(records):

        return sum(
            record.calculate_projection()
            for record in records
            if record.item_type == "wine"
        )

    @staticmethod
    def grape_projection(records):

        return sum(
            record.calculate_projection()
            for record in records
            if record.item_type == "table_grapes"
        )