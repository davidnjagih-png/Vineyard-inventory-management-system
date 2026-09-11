class WineForecast:
    """
    Handles wine production and revenue forecasting.

    Business Rules:
    - 1.5 kg wine grapes = 1 litre wine
    - 750 ml = 1 bottle
    """

    WINE_PRICES = {
        "red": 750,
        "white": 700,
        "rose": 650
    }

    @staticmethod
    def estimate_litres(grape_quantity_kg):
        """
        1.5 kg grapes = 1 litre wine
        """
        return round(grape_quantity_kg / 1.5, 2)

    @staticmethod
    def estimate_bottles(litres):
        """
        750 ml = 1 bottle
        """
        return int(litres / 0.75)

    @classmethod
    def estimate_revenue(cls, wine_type, bottle_quantity):
        price = cls.WINE_PRICES.get(wine_type.lower(), 0)
        return bottle_quantity * price

    @classmethod
    def generate_forecast(cls, wine_type, grape_quantity):
        litres = cls.estimate_litres(grape_quantity)
        bottles = cls.estimate_bottles(litres)
        revenue = cls.estimate_revenue(wine_type, bottles)

        return {
            "wine_type": wine_type,
            "grapes_kg": grape_quantity,
            "litres": litres,
            "bottles": bottles,
            "estimated_revenue": revenue
        }