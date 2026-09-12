class GrapeStock:
    valid_varieties = {"red", "white", "rose"}

    def __init__(self, grape_type, quantity, quality=None, variety=None):
        if grape_type == "wine" and variety not in self.valid_varieties:
            raise ValueError("Wine grape must be red, white or rose variety")

            
        self._grape_type = grape_type
        self._quantity = quantity
        self._quality = quality
        self._variety = variety
    
    def remove_quantity(self, quantity):
        if quantity > self._quantity:
            raise ValueError("Cannot remove more than available")
        
        self._quantity -= quantity 

    
    @property
    def grape_type(self):
        return self._grape_type
    
    @property
    def quantity(self):
        return self._quantity
    
    @property
    def quality(self):
        return self._quality
    
    @property
    def variety(self):
        return self._variety
    