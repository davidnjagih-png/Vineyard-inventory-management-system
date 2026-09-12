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


def test_add_grape_stock():
    pass


def test_remove_grape_stock():
    pass


def test_cannot_remove_more_grapes_than_available():
    pass


def test_add_wine_batch_invalid_types():
    inventory = Inventory()

    with pytest.raises(ValueError):
        inventory.add_wine_batch("B002", "sparkling", 2024, 150)
