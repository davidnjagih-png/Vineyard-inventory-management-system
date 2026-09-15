from models.wine_batch import WineBatch

def test_wine_batch_accepts_red():
    batch = WineBatch("red", 2024, 150)

    assert batch.type == "red"

def test_wine_batch_accepts_white():
    batch = WineBatch("white", 2024, 150)

    assert batch.type == "white"

def test_wine_batch_accepts_rose():
    batch = WineBatch("rose", 2024, 150)

    assert batch.type == "rose"

def test_wine_batch_stores_vintage():
    batch = WineBatch("red", 2024, 150)

    assert batch.vintage == 2024

def test_wine_batch_stores_quantity():
    batch = WineBatch("red", 2024, 150)

    assert batch.quantity == 150

def test_estimated_wine_production():
    batch = WineBatch("red", 2024, 150)

    # 1.5 kg of grapes = 1 litre of wine
    assert batch.estimated_litres() == 100

def test_estimated_bottles():
    batch = WineBatch("red", 2024, 150)

    # 100 litres = 100,000 ml
    # 100,000 / 750 = 133.33 bottles
    assert batch.estimated_bottles() == 133.33

def test_estimated_wine_value():
    batch = WineBatch("red", 2024, 150)

    # 133.33 bottles × 1200 KSh
    assert batch.estimated_value() == 159996