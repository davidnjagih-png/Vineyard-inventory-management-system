def generate_sales_report(records):
    """Generate combined sales report for wine and grapes."""
    wine_sales = sum(r.calculate_projection() for r in records if "wine" in r.item.lower())
    grape_sales = sum(r.calculate_projection() for r in records if "grape" in r.item.lower())
    total_sales = wine_sales + grape_sales

    return {
        "wine_sales": wine_sales,
        "grape_sales": grape_sales,
        "total_sales": total_sales
    }
