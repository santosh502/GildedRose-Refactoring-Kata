
class Item:
    """
    Represents an item in the Gilded Rose inventory.
    Attributes:
        name (str): Name of the item
        sell_in (int): Number of days we have to sell the item
        quality (int): How valuable the item is
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

