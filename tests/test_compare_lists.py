from unittest import TestCase
from inventory_auditor.compare_lists import compare

class TestCompareList(TestCase):
	def test_list_equal(self,):
		physical_inventory = {
			"ABC":3,
			"DEF":4,
		}
		digital_inventory = {
			"DEF":4,
			"ABC":3,
		}
		discrepencies = compare(physical_inventory,digital_inventory)
		self.assertEqual(discrepencies, {})
		
	def test_list_not_equal(self,):
		physical_inventory = {
			"ABC":3,
			"DEF":4,
		}
		digital_inventory = {
			"DEF":4,
			"ABC":5,
		}
		discrepencies = compare(physical_inventory,digital_inventory)
		self.assertEqual(discrepencies, {
			"ABC":{
				"physical":3,
				"digital":5,
			}
		})
		
	def test_missing_from_physical(self,):
		physical_inventory = {
			"ABC":3,
			"DEF":4,
		}
		digital_inventory = {
			"DEF":4,
			"ABC":3,
			"GHI":2,
		}
		discrepencies = compare(physical_inventory,digital_inventory)
		self.assertEqual(discrepencies, {
			"GHI":{
				"physical":None,
				"digital":2,
			}
		})
		
	def test_missing_from_digital(self,):
		physical_inventory = {
			"ABC":3,
			"DEF":4,
			"GHI":2,
		}
		digital_inventory = {
			"DEF":4,
			"ABC":3,
		}
		discrepencies = compare(physical_inventory,digital_inventory)
		self.assertEqual(discrepencies, {
			"GHI":{
				"physical":2,
				"digital":None,
			}
		})
		
	def test_case_sensitivity(self,):
		physical_inventory = {
			"ABC":3,
			"DeF":4,
		}
		digital_inventory = {
			"ABC":3,
			"DEF":4,
		}
		discrepencies = compare(physical_inventory,digital_inventory)
		self.assertEqual(discrepencies, {
			"DeF":{
				"physical":4,
				"digital":None,
			},
			"DEF":{
				"physical":None,
				"digital":4,
			}
		})
	
	def test_bug(self,):
		physical_inventory = {
			"ABC":3,
		}
		digital_inventory = {
			"ABC":6,
			"DEF":5,
		}
		discrepencies = compare(physical_inventory,digital_inventory)
		self.assertEqual(discrepencies, {
			"ABC":{
				"physical":3,
				"digital":6,
			},
			"DEF":{
				"physical":None,
				"digital":5,
			}
		})