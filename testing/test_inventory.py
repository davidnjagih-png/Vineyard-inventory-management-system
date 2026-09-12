import pytest
from lib.inventory import Inventory

def test_add_wine_batch():
    inventory = Inventory()

    inventory.add_wine_batch("B001", "red", 2024, 150)

    batches = inventory.get_wine_batches()

    assert len(batches) == 1

def test_wine_batch_has_correct_details():
    inventory = Inventory()

    inventory.add_wine_batch("B001", "red", 2024, 150)

    batch = inventory.get_wine_batches()[0]

    assert batch.batch_id == "B001"
    assert batch.wine_type == "red"
    assert batch.vintage == 2024
    assert batch.quantity == 150

def test_add_wine_batch_negative_quantity():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.add_wine_batch("B003", "red", 2024, -10)

def test_duplicate_wine_batch_id():
    inventory = Inventory()

    inventory.add_wine_batch("B001", "red", 2024, 150)

    with pytest.raises(ValueError):
        inventory.add_wine_batch("B001", "white", 2024, 300)

def test_edit_wine_batch():
    inventory = Inventory()

    inventory.add_wine_batch("B001", "red", 2024, 150)

    inventory.edit_wine_batch(
        "B001",
        wine_type = "white",
        vintage=2025,
        quantity=200
    )

    batch = inventory.get_wine_batch("B001")

    assert batch.batch_id == "B001"
    assert batch.wine_type == "white"
    assert batch.vintage == 2025
    assert batch.quantity == 200

def test_edit_nonexistent_wine_batch():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.edit_wine_batch(
            "B999",
            wine_type = "red",
            vintage = 2025,
            quantity = 100
        )

def test_delete_wine_batch():
    inventory = Inventory()

    inventory.add_wine_batch("B001", "red", 2024, 150)

    inventory.delete_wine_batch("B001")

    assert inventory.get_wine_batches() == []


def test_add_wine_batch_invalid_types():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.add_wine_batch("B002", "sparkling", 2024, 150)

def test_add_grape_stock():
    inventory = Inventory()

    inventory.add_grape_stock("table", 100)

    stock = inventory.get_grape_stock("table")

    assert stock.grape_type == "table"
    assert stock.quantity == 100

def test_remove_grape_stock():
    inventory = Inventory()

    inventory.add_grape_stock("table", 100)

    inventory.remove_grape_stock("table", 30)

    stock = inventory.get_grape_stock("table")

    assert stock.quantity == 70

def test_cannot_remove_more_grapes_than_available():
    inventory = Inventory()

    inventory.add_grape_stock("table", 100)

    with pytest.raises(ValueError):
        inventory.remove_grape_stock("table", 150)

def test_grape_stock_quality():
    inventory = Inventory()

    inventory.add_grape_stock("table", 100, "good")

    stock = inventory.get_grape_stock("table")

    assert stock.grape_type == "table"
    assert stock.quantity == 100
    assert stock.quality == "good"

def test_wine_grape_variety():
    inventory = Inventory()

    inventory.add_grape_stock("wine", 500, "good", "red")

    stock = inventory.get_grape_stock("wine")

    assert stock.grape_type == "wine"
    assert stock.quantity == 500
    assert stock.quality == "good"
    assert stock.variety == "red"

def test_invalid_wine_grape_variety():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.add_grape_stock("wine", 500, "good", "green")