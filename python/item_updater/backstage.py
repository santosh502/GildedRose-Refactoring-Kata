from .base import ItemUpdater


class BackstagePassUpdater(ItemUpdater):
    """
    Updater for 'Backstage passes', which increase in quality as the sell-in date approaches,
    but drops to 0 after the concert.
    """
    def update(self):
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.increase_quality(3)
        elif self.item.sell_in < 10:
            self.increase_quality(2)
        else:
            self.increase_quality()