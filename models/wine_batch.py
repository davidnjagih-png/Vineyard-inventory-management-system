class WineBatch:
    def __init__(self, type, vintage, quantity):
        self.type = type
        self.vintage = vintage
        self.quantity = quantity

    def estimated_litres(self):
        # 1.5 kg of wine grapes = 1 litre of wine
        litres = self.quantity / 1.5
        return litres

    def estimated_bottles(self):
        # 1 bottle = 750 ml
        # 1 litre = 1000 ml
        litres = self.estimated_litres()
        bottles = (litres * 1000) / 750

        return round(bottles, 2)

    def estimated_value(self):
        # 1 bottle = 1200 KSh
        bottles = self.estimated_bottles()
        return round(bottles * 1200)