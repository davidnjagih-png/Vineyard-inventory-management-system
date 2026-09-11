from models.lib.sales_record.sales_record import SalesRecord

from logic.forecasting.sales_projection import (
    SalesProjection
)

from logic.forecasting.inventory_alerts import (
    InventoryAlerts
)

from logic.forecasting.recommendations import (
    Recommendations
)

from logic.forecasting.forecasting_service import (
    ForecastingService
)


# ------------------------------------------------------------------
# Mock Classes
# ------------------------------------------------------------------

class MockWineBatch:

    def __init__(self, record_type, quantity):
        self.record_type = record_type
        self.quantity = quantity


class MockGrapeStock:

    def __init__(self, category, quantity):
        self.category = category
        self.quantity = quantity


# ------------------------------------------------------------------
# Test Data
# ------------------------------------------------------------------

def get_sales_records():
    return [
        SalesRecord(
            item="red wine",
            quantity=100,
            price_per_unit=750
        ),
        SalesRecord(
            item="white wine",
            quantity=50,
            price_per_unit=700
        ),
        SalesRecord(
            item="table grapes",
            quantity=200,
            price_per_unit=120
        )
    ]


# ------------------------------------------------------------------
# Sales Projection Tests
# ------------------------------------------------------------------

def test_total_revenue():

    records = get_sales_records()

    assert (
        SalesProjection.total_revenue(records)
        == 134000
    )


def test_wine_revenue():

    records = get_sales_records()

    assert (
        SalesProjection.wine_revenue(records)
        == 110000
    )


def test_grape_revenue():

    records = get_sales_records()

    assert (
        SalesProjection.grape_revenue(records)
        == 24000
    )


def test_revenue_by_product():

    records = get_sales_records()

    revenue = (
        SalesProjection.revenue_by_product(
            records
        )
    )

    assert revenue["red wine"] == 75000
    assert revenue["white wine"] == 35000
    assert revenue["table grapes"] == 24000


def test_top_selling_product():

    records = get_sales_records()

    assert (
        SalesProjection.top_selling_product(
            records
        )
        == "red wine"
    )


def test_generate_report():

    records = get_sales_records()

    report = (
        SalesProjection.generate_report(
            records
        )
    )

    assert report["total_revenue"] == 134000
    assert report["top_selling_product"] == "red wine"


# ------------------------------------------------------------------
# Inventory Alert Tests
# ------------------------------------------------------------------

def test_wine_stock_alerts():

    wine_batches = [
        MockWineBatch("red", 25)
    ]

    alerts = (
        InventoryAlerts.wine_stock_alerts(
            wine_batches
        )
    )

    assert len(alerts) == 1
    assert "low wine stock" in alerts[0].lower()


def test_grape_stock_alerts():

    grape_stock = [
        MockGrapeStock(
            "table grapes",
            10
        )
    ]

    alerts = (
        InventoryAlerts.grape_stock_alerts(
            grape_stock
        )
    )

    assert len(alerts) == 1
    assert "low grape stock" in alerts[0].lower()


def test_generate_alerts():

    wine_batches = [
        MockWineBatch("rose", 20)
    ]

    grape_stock = [
        MockGrapeStock(
            "table grapes",
            15
        )
    ]

    alerts = (
        InventoryAlerts.generate_alerts(
            wine_batches,
            grape_stock
        )
    )

    assert len(alerts) == 2


# ------------------------------------------------------------------
# Recommendation Tests
# ------------------------------------------------------------------

def test_sales_recommendation():

    records = get_sales_records()

    recommendation = (
        Recommendations.sales_recommendation(
            records
        )
    )
    
