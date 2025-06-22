from .base import ItemUpdater


class NormalItemUpdater(ItemUpdater):
    """Updater for normal items that degrade in quality over time."""
    def update(self):
        self.decrease_sell_in()
        degrade = 1 if self.item.sell_in >= 0 else 2
        self.decrease_quality(degrade)