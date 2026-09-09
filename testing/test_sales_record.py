import pytest
from models.sales_record import SalesRecord

def test_sales_record_creation():
    
    record = SalesRecord(item="red wine", quantity=50, price=10)
    assert record.item == "red wine"
    assert record.quantity == 50
    assert record.price == 10


