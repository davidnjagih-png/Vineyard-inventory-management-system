def price_wine(wine_type, quantity, price_per_unit):
    """Return pricing details for wine batches."""
    return {
        "wine_type": wine_type,
        "quantity": quantity,
        "price_per_unit": price_per_unit,
        "total": quantity * price_per_unit
    }

def price_grapes(quantity, price_per_unit):
    """Return pricing details for table grapes."""
    return {
        "item": "table grapes",
        "quantity": quantity,
        "price_per_unit": price_per_unit,
        "total": quantity * price_per_unit
    }
