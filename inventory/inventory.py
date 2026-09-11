from .wine_batch import WineBatch

class Inventory:
    def __init__(self):
        self._wine_batches = []
    
    def add_wine_batch(self, batch_id, wine_type, vintage, quantity):
        batch = WineBatch(
            batch_id,
            wine_type,
            vintage,
            quantity
        )

        
        self._wine_batches.append(batch)
    
    def get_wine_batches(self):
        return self._wine_batches