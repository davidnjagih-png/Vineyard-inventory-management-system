from models.wine_batch import WineBatch


def test_wine_batch_stores_type():
    batch = WineBatch("Red Wine", 2024, 500)

    assert batch.type == "Red Wine"


def test_wine_batch_stores_year():
    batch = WineBatch("Red Wine", 2024, 500)

    assert batch.year == 2024


def test_wine_batch_stores_quantity():
    batch = WineBatch("Red Wine", 2024, 500)

    assert batch.quantity == 500


def test_wine_batch_stores_all_details():
    batch = WineBatch("White Wine", 2025, 1000)

    assert batch.type == "White Wine"
    assert batch.year == 2025
    assert batch.quantity == 1000