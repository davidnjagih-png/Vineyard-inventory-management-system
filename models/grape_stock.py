class GrapeStock:
    def __init__(self, category, quantity, quality, variety=None):
        self.category = category
        self.quantity = quantity
        self.quality = quality
        self.variety = variety

    def estimated_packets(self):
        # 1 kg of table grapes = 2 packets
        packets = self.quantity * 2
        return packets

    def estimated_value(self):
        # 1 packet of grapes = 350 KSh
        packets = self.estimated_packets()
        return packets * 350