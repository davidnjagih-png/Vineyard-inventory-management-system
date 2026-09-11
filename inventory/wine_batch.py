class WineBatch:
    valid_types = {"red", "white", "rose"}


    def __init__(self, batch_id, wine_type, vintage, quantity):
        if wine_type not in self.valid_types:
             raise ValueError("Wine type must be red, white or rose")

        self._batch_id = batch_id
        self._wine_type = wine_type
        self._vintage = vintage
        self._quantity = quantity

    @property
    def batch_id(self):
        return self._batch_id

    
    @property
    def wine_type(self):
        return self._wine_type


    
    @property
    def vintage(self):
        return self._vintage


    
    @property
    def quantity(self):
        return self._quantity
