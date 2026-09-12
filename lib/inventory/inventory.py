from .wine_batch import WineBatch
from .grape_stock import GrapeStock

class Inventory:
    def __init__(self):
        self._wine_batches = []
        self._grape_stock = []
    
    def add_wine_batch(self, batch_id, wine_type, vintage, quantity):
        for batch in self._wine_batches:
            if batch.batch_id == batch_id:
                raise ValueError("Batch Id already exists")
                
        batch = WineBatch(
            batch_id,
            wine_type,
            vintage,
            quantity
        )

        
        self._wine_batches.append(batch)
    
    def get_wine_batches(self):
        return self._wine_batches
    
    def get_wine_batch(self, batch_id):
        for batch in self._wine_batches:
            if batch.batch_id == batch_id:
                return batch
        
        raise ValueError("wine batch not found.")
    
    def edit_wine_batch(self, batch_id, wine_type, vintage, quantity):
        for batch in self._wine_batches:
            if batch.batch_id == batch_id:
                batch.update_details(wine_type, vintage, quantity)
                return
        
        raise ValueError("Batch not found.")
    
    def delete_wine_batch(self, batch_id):
        for batch in self._wine_batches:
            if batch.batch_id == batch_id:
                self._wine_batches.remove(batch)
                return
        
        raise ValueError("wine batch not found.")
    
    def add_grape_stock(self, grape_type, quantity, quality=None, variety=None):
        stock = GrapeStock(grape_type, quantity, quality, variety)
        self._grape_stock.append(stock)

    def get_grape_stock(self, grape_type):
        for stock in self._grape_stock:
            if stock.grape_type == grape_type:
                return stock
        
        raise ValueError("Grape stock not found.")
    
    def remove_grape_stock(self, grape_type, quantity):
        for stock in self._grape_stock:
            if stock.grape_type == grape_type:
                stock.remove_quantity(quantity)
                return
        
        raise ValueError("grape stock not found.")
        
