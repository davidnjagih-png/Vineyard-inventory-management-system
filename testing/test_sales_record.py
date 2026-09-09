import pytest
from models.sales_record import SalesRecord

# --- Sales Projections: Wine ---

def test_view_wine_sales_projection():
    record = SalesRecord(item="red wine", quantity=100, price_per_unit=750)  # price per bottle in KES
    projection = record.calculate_projection()
    assert projection == 100 * 750

def test_price_wine_by_type():
    record = SalesRecord(item="rose wine", quantity=50, price_per_unit=600)
    assert record.item == "rose wine"
    assert record.price_per_unit == 600
    assert record.calculate_projection() == 50 * 600

# --- Sales Projections: Table Grapes ---

def test_view_table_grape_projection():
    record = SalesRecord(item="table grapes", quantity=40, price_per_unit=100)  # price per packet
    projection = record.calculate_projection()
    assert projection == 40 * 100

def test_price_table_grapes_by_packet():
    record = SalesRecord(item="table grapes", quantity=10, price_per_unit=120)
    assert record.item == "table grapes"
    assert record.calculate_projection() == 10 * 120

# --- Reports ---

def test_generate_sales_report():
    wine = SalesRecord(item="white wine", quantity=20, price_per_unit=700)
    grapes = SalesRecord(item="table grapes", quantity=15, price_per_unit=90)

    report = {
        "wine_sales": wine.calculate_projection(),
        "grape_sales": grapes.calculate_projection(),
        "total_sales": wine.calculate_projection() + grapes.calculate_projection()
    }

    assert report["wine_sales"] == 20 * 700
    assert report["grape_sales"] == 15 * 90
    assert report["total_sales"] == (20 * 700) + (15 * 90)
