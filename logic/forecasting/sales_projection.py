class SalesProjection:
    """
    Handles sales projections and reporting
    using SalesRecord objects.
    """

    @staticmethod
    def total_revenue(records):
        """
        Calculate total projected revenue.
        """
        return sum(
            record.calculate_projection()
            for record in records
        )

    @staticmethod
    def wine_revenue(records):
        """
        Calculate wine revenue.
        """
        return sum(
            record.calculate_projection()
            for record in records
            if "wine" in record.item.lower()
        )

    @staticmethod
    def grape_revenue(records):
        """
        Calculate table grape revenue.
        """
        return sum(
            record.calculate_projection()
            for record in records
            if "grape" in record.item.lower()
        )

    @staticmethod
    def revenue_by_product(records):
        """
        Revenue grouped by product.
        """

        products = {}

        for record in records:

            if record.item not in products:
                products[record.item] = 0

            products[record.item] += (
                record.calculate_projection()
            )

        return products

    @staticmethod
    def top_selling_product(records):
        """
        Returns highest earning product.
        """

        revenue = (
            SalesProjection.revenue_by_product(
                records
            )
        )

        if not revenue:
            return None

        return max(
            revenue,
            key=revenue.get
        )

    @staticmethod
    def generate_report(records):
        """
        Generates complete sales report.
        """

        return {
            "total_revenue":
                SalesProjection.total_revenue(
                    records
                ),

            "wine_revenue":
                SalesProjection.wine_revenue(
                    records
                ),

            "grape_revenue":
                SalesProjection.grape_revenue(
                    records
                ),

            "revenue_by_product":
                SalesProjection.revenue_by_product(
                    records
                ),

            "top_selling_product":
                SalesProjection.top_selling_product(
                    records
                )
        }