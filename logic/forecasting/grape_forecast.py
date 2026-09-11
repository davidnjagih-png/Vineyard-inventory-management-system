class GrapeForecast:
    """
    Handles table grape packet and revenue forecasting.
    """

    MARKET_PRICE_PER_PACKET = 120

    @staticmethod
    def estimate_packets(quantity_kg):
        """
        1 kg grapes = 2 packets
        """
        return quantity_kg * 2

    @classmethod
    def estimate_revenue(cls, quantity_kg):
        packets = cls.estimate_packets(quantity_kg)

        return packets * cls.MARKET_PRICE_PER_PACKET

    @classmethod
    def generate_forecast(cls, quantity_kg):
        packets = cls.estimate_packets(quantity_kg)
        revenue = cls.estimate_revenue(quantity_kg)

        return {
            "quantity_kg": quantity_kg,
            "packets": packets,
            "estimated_revenue": revenue
        }