# -*- coding: utf-8 -*-

class GildedRose(object):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    CONJURED = "Conjured"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # does quality decrease or increase over time? default is decrease
            # default value -1
            quality_direction = -1
            # the amount that quality changes over time. default value 1
            quality_delta = 1
            # Conjured items degrade in quality twice as fast as normal items
            if item.name.startswith(GildedRose.CONJURED):
                quality_delta = 2
            # all items must bend to time - except for the legendary item Sulfuras
            if item.name != GildedRose.SULFURAS:
                item.sell_in = item.sell_in - 1
            # Aged Brie and Backstage Passes actually increase in quality over time
            if item.name == GildedRose.AGED_BRIE or item.name == GildedRose.BACKSTAGE_PASSES:
                quality_direction = 1
            # Backstage Passes incrementally gain in value as we get closer to
            # the concert date
            if item.name == GildedRose.BACKSTAGE_PASSES:
                if item.sell_in < 11:
                    quality_delta = 2
                if item.sell_in < 6:
                    quality_delta = 3
            # Once the sell date has passed, quality degrades twice as fast
            if item.sell_in < 0:
                quality_delta = quality_delta * 2

            if item.name != GildedRose.SULFURAS:
                item.quality = item.quality + (quality_direction * quality_delta)
                # quality can never be negative and expired backstage passes are
                # worthless
                if item.quality < 0 or (item.name == GildedRose.BACKSTAGE_PASSES
                        and item.sell_in < 0):
                    item.quality = 0
                # quality can never be greater than 50
                if item.quality > 50:
                    item.quality = 50

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
