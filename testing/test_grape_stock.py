from models.grape_stock import GrapeStock


def test_table_grapes_category():
    grapes = GrapeStock("table grapes", 10, "good")

    assert grapes.category == "table grapes"


def test_wine_grapes_category():
    grapes = GrapeStock("wine grapes", 10, "good")

    assert grapes.category == "wine grapes"


def test_grape_stock_stores_quantity():
    grapes = GrapeStock("table grapes", 10, "good")

    assert grapes.quantity == 10


def test_grape_stock_stores_quality():
    grapes = GrapeStock("table grapes", 10, "good")

    assert grapes.quality == "good"


def test_wine_grape_red_variety():
    grapes = GrapeStock("wine grapes", 10, "good", "red")

    assert grapes.variety == "red"


def test_wine_grape_white_variety():
    grapes = GrapeStock("wine grapes", 10, "good", "white")

    assert grapes.variety == "white"


def test_wine_grape_rose_variety():
    grapes = GrapeStock("wine grapes", 10, "good", "rose")

    assert grapes.variety == "rose"


def test_table_grape_packets():
    grapes = GrapeStock("table grapes", 10, "good")

    # 1 kg = 2 packets
    assert grapes.estimated_packets() == 20


def test_table_grape_value():
    grapes = GrapeStock("table grapes", 10, "good")

    # 20 packets × 350 KSh
    assert grapes.estimated_value() == 7000