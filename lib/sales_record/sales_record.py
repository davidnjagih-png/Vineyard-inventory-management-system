import pytest
from lib.sales_record.sales_record import SalesRecord
from lib.sales_record.reporting import generate_sales_report

def test_view_wine_sales_projection():
    record = SalesRecord(item="red wine", quantity=100, price_per_unit=750)
    projection = record.calculate_projection()
    assert projection == 100 * 750

def test_price_wine_by_type():
    record = SalesRecord(item="rose wine", quantity=50, price_per_unit=600)
    assert record.item == "rose wine"
    assert record.price_per_unit == 600
    assert record.calculate_projection() == 50 * 600

def test_view_table_grape_projection():
    record = SalesRecord(item="table grapes", quantity=40, price_per_unit=100)
    projection = record.calculate_projection()
    assert projection == 40 * 100

def test_price_table_grapes_by_packet():
    record = SalesRecord(item="table grapes", quantity=10, price_per_unit=120)
    assert record.item == "table grapes"
    assert record.calculate_projection() == 10 * 120

def test_generate_sales_report():
    wine = SalesRecord(item="white wine", quantity=20, price_per_unit=700)
    grapes = SalesRecord(item="table grapes", quantity=15, price_per_unit=90)

    report = generate_sales_report([wine, grapes])

    assert report["wine_sales"] == 20 * 700
    assert report["grape_sales"] == 15 * 90
    assert report["total_sales"] == (20 * 700) + (15 * 90)
