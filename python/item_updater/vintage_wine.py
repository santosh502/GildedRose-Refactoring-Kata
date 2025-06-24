from .base import ItemUpdater


class VintageWineUpdater(ItemUpdater):
    """Updater for vintage wine items that update time by1 when expired"""
    def update(self):
        if self.item.sell_in <= 0:
            upgrade = 2
            sell_in = 0
        else:
            upgrade = 0
            sell_in = 1
        self.decrease_sell_in(sell_in=sell_in)
        self.increase_quality(upgrade)