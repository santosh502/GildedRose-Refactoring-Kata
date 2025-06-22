import unittest
from ..gilded_rose import GildedRose
from ..item import Item
from ..constants import AGED_BRIE, SULFURAS, BACKSTAGE_PASS, CONJURED_KEYWORD

class GildedRoseTest(unittest.TestCase):
    """
    Comprehensive unit tests for GildedRose update logic, covering all item types.
    """

    def test_normal_item_before_sell_date(self):
        items = [Item("Normal Item", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 9)
        self.assertEqual(items[0].quality, 19)

    def test_normal_item_on_sell_date(self):
        items = [Item("Normal Item", 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, -1)
        self.assertEqual(items[0].quality, 18)

    def test_normal_item_after_sell_date(self):
        items = [Item("Normal Item", -1, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, -2)
        self.assertEqual(items[0].quality, 18)

    def test_normal_item_quality_never_negative(self):
        items = [Item("Normal Item", 5, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_aged_brie_before_sell_date(self):
        items = [Item(AGED_BRIE, 2, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 1)
        self.assertEqual(items[0].quality, 1)

    def test_aged_brie_after_sell_date(self):
        items = [Item(AGED_BRIE, 0, 0)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 2)

    def test_aged_brie_quality_does_not_exceed_50(self):
        items = [Item(AGED_BRIE, 0, 49)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_does_not_change(self):
        items = [Item(SULFURAS, 0, 80)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].sell_in, 0)
        self.assertEqual(items[0].quality, 80)

    def test_backstage_pass_long_before_concert(self):
        items = [Item(BACKSTAGE_PASS, 15, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 21)

    def test_backstage_pass_medium_close_to_concert(self):
        items = [Item(BACKSTAGE_PASS, 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 22)

    def test_backstage_pass_very_close_to_concert(self):
        items = [Item(BACKSTAGE_PASS, 5, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 23)

    def test_backstage_pass_after_concert(self):
        items = [Item(BACKSTAGE_PASS, 0, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_conjured_item_before_sell_date(self):
        items = [Item(f"{CONJURED_KEYWORD} Mana Cake", 5, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 8)

    def test_conjured_item_on_sell_date(self):
        items = [Item(f"{CONJURED_KEYWORD} Mana Cake", 0, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 6)

    def test_conjured_item_after_sell_date(self):
        items = [Item(f"{CONJURED_KEYWORD} Mana Cake", -1, 10)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 6)

    def test_conjured_item_quality_never_negative(self):
        items = [Item(f"{CONJURED_KEYWORD} Mana Cake", 0, 1)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(items[0].quality, 0)


if __name__ == '__main__':
    unittest.main()
