# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_normal_item_degradation(self):
        # Check that run of the mill items drop their quality by one with every
        # invocation of update_quality if they have positive values for sell_in
        items = [Item("Gruel", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(9, items[0].quality)

    def test_expired_item_degradation(self):
        # Check that run of the mill items drop their quality by two with every
        # invocation of update_quality if they have negative values for sell_in
        items = [Item("Gruel", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(8, items[0].quality)

    def test_quality_never_negative(self):
        # Check that run of the mill items never achieve negative quality
        items = [Item("Gruel", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_quality_cap(self):
        # Check that run of the mill items never end up with a quality greater
        # than 50 after one iteration
        items = [Item("Gruel", 0, 60)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_aged_brie_ages_normally(self):
        # Check that Aged Brie increases in quality by 1 when sell_in is
        # positive
        items = [Item(GildedRose.AGED_BRIE, 5, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_aged_brie_ages_rapidly(self):
        # Check that Aged Brie increases in quality by 2 when sell_in is
        # negative
        items = [Item(GildedRose.AGED_BRIE, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(12, items[0].quality)
        self.assertEquals(-1, items[0].sell_in)

    def test_aged_brie_quality_cap(self):
        # Check that Aged Brie increases in quality over time, but only up to a
        # maximum quality of 50
        items = [Item(GildedRose.AGED_BRIE, 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfuras_is_awesome(self):
        # Check that Sulfuras is unaffected by the passing of time; neither its
        # sell_in nor its quality ever changes.
        items = [Item(GildedRose.SULFURAS, 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(80, items[0].quality)
        self.assertEquals(5, items[0].sell_in)

    def test_backstage_passes_gain_value_over_time(self):
        # Check that Backstage passes increases in quality by 1 when sell_in is
        # positive and greater than 10
        items = [Item(GildedRose.BACKSTAGE_PASSES, 15, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)

    def test_backstage_passes_gain_more_value_a_week_before(self):
        # Check that Backstage passes increases in quality by 2 when sell_in is
        # positive and less than or equal to 10 but greater than 5
        items = [Item(GildedRose.BACKSTAGE_PASSES, 7, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(2, items[0].quality)

    def test_backstage_passes_gain_even_more_value_a_few_days_before(self):
        # Check that Backstage passes increases in quality by 3 when sell_in is
        # positive and less than or equal to 5 but greater than 0
        items = [Item(GildedRose.BACKSTAGE_PASSES, 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(3, items[0].quality)

    def test_backstage_passes_are_worthless_once_expired(self):
        # Check that Backstage passes are not worthy diddly squat after they
        # have expired
        items = [Item(GildedRose.BACKSTAGE_PASSES, 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_backstage_passes_quality_cap(self):
        # Check that Backstage passes never get to quality greater than 50
        items = [Item(GildedRose.BACKSTAGE_PASSES, 2, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_conjured_item_degradation(self):
        # Check that conjured items drop their quality by two with every
        # invocation of update_quality if they have positive values for sell_in
        items = [Item("Conjured Gruel", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(8, items[0].quality)

    def test_expired_conjured_item_degradation(self):
        # Check that conjured items drop their quality by four with every
        # invocation of update_quality if they have negative values for sell_in
        items = [Item("Conjured Gruel", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(6, items[0].quality)

    def test_expired_conjured_item_quality_floor(self):
        # Check that conjured items dont drop their quality below zero, even if
        # expired.
        items = [Item("Conjured Gruel", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
