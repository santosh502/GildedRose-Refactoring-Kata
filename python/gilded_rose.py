

from .item_updater.brie import AgedBrieUpdater
from .item_updater.sulfuras import SulfurasUpdater
from .item_updater.backstage import BackstagePassUpdater
from .item_updater.conjured import ConjuredItemUpdater
from .item_updater.normal import NormalItemUpdater


class GildedRose:
    """
    The main class that holds the list of items and updates them daily using appropriate strategies.
    """
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update quality for each item using its corresponding updater."""
        for item in self.items:
            self.get_updater(item).update()

    def get_updater(self, item):
        """
        Return the appropriate updater instance based on the item name.
        """
        if item.name == "Aged Brie":
            return AgedBrieUpdater(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater(item)
        elif "Conjured" in item.name:
            return ConjuredItemUpdater(item)
        else:
            return NormalItemUpdater(item)

