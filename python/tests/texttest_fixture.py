from gilded_rose import GildedRose
from item import Item
from constants import AGED_BRIE, SULFURAS, BACKSTAGE_PASS, CONJURED_KEYWORD

if __name__ == "__main__":
    print("OMGHAI!")

    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
        Item(name=AGED_BRIE, sell_in=2, quality=0),
        Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
        Item(name=SULFURAS, sell_in=0, quality=80),
        Item(name=SULFURAS, sell_in=-1, quality=80),
        Item(name=BACKSTAGE_PASS, sell_in=15, quality=20),
        Item(name=BACKSTAGE_PASS, sell_in=10, quality=49),
        Item(name=BACKSTAGE_PASS, sell_in=5, quality=49),
        Item(name=f"{CONJURED_KEYWORD} Mana Cake", sell_in=3, quality=6),
    ]

    import sys
    days = int(sys.argv[1]) + 1 if len(sys.argv) > 1 else 2
    for day in range(days):
        print(f"-------- day {day} --------")
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
