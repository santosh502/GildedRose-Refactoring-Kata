class ItemUpdater:
    """
    Abstract base class for all item updaters.
    Each subclass should implement the update() method to apply specific rules.
    """
    def __init__(self, item):
        self.item = item

    def update(self):
        """Update the item. Must be implemented by subclasses."""
        raise NotImplementedError

    def increase_quality(self, amount=1):
        """Increase item quality by amount (max 50)."""
        self.item.quality = min(50, self.item.quality + amount)

    def decrease_quality(self, amount=1):
        """Decrease item quality by amount (min 0)."""
        self.item.quality = max(0, self.item.quality - amount)

    def decrease_sell_in(self, sell_in=1):
        """Decrease the sell_in value by 1."""
        self.item.sell_in -= sell_in
