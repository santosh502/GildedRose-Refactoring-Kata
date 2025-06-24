

from .constants import (AGED_BRIE, BACKSTAGE_PASS, CONJURED_KEYWORD, SULFURAS,
                        VINTAGE_WINE)
from .item_updater.backstage import BackstagePassUpdater
from .item_updater.brie import AgedBrieUpdater
from .item_updater.conjured import ConjuredItemUpdater
from .item_updater.normal import NormalItemUpdater
from .item_updater.sulfuras import SulfurasUpdater
from .item_updater.vintage_wine import VintageWineUpdater


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
        if item.name == AGED_BRIE:
            return AgedBrieUpdater(item)
        elif item.name == SULFURAS:
            return SulfurasUpdater(item)
        elif item.name == BACKSTAGE_PASS:
            return BackstagePassUpdater(item)
        elif CONJURED_KEYWORD in item.name:
            return ConjuredItemUpdater(item)
        elif item.name == VINTAGE_WINE:
            return VintageWineUpdater(item)
        else:
            return NormalItemUpdater(item)

