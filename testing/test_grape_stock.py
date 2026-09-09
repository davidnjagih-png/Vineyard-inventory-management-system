from models.grape_stock import GrapeStock


def test_grape_stock_stores_category():
    grapes = GrapeStock("table", 500)

    assert grapes.category == "table"


def test_grape_stock_stores_quantity():
    grapes = GrapeStock("wine", 1000)

    assert grapes.quantity == 1000


def test_table_grape_stock():
    grapes = GrapeStock("table", 500)

    assert grapes.category == "table"
    assert grapes.quantity == 500


def test_wine_grape_stock():
    grapes = GrapeStock("wine", 1000)

    assert grapes.category == "wine"
    assert grapes.quantity == 1000