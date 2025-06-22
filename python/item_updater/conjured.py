from .base import ItemUpdater


class ConjuredItemUpdater(ItemUpdater):
    """
    Updater for 'Conjured' items, which degrade in quality twice as fast as normal items.
    """
    def update(self):
        self.decrease_sell_in()
        degrade = 2 if self.item.sell_in >= 0 else 4
        self.decrease_quality(degrade)