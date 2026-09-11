class SalesProjection:
    """
    Generates sales projections from SalesRecord data.
    """

    @staticmethod
    def total_projection(records):
        return sum(
            record.calculate_projection()
            for record in records
        )

    @staticmethod
    def projection_by_category(records):
        projections = {}

        for record in records:
            category = record.item_type

            if category not in projections:
                projections[category] = 0

            projections[category] += (
                record.calculate_projection()
            )

        return projections

    @staticmethod
    def generate_report(records):

        return {
            "total_sales_projection":
                SalesProjection.total_projection(records),

            "category_breakdown":
                SalesProjection.projection_by_category(records)
        }