from .base import ItemUpdater


class AgedBrieUpdater(ItemUpdater):
    """Updater for 'Aged Brie', which increases in quality as it ages."""
    def update(self):
        self.decrease_sell_in()
        self.increase_quality(2 if self.item.sell_in < 0 else 1)