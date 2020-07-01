from unittest import TestCase
from inventory_auditor.format_discrepancies import format

class TestFormatDiscrepancies(TestCase):
	def test_no_discrepancies(self,):
		message = format({})
		self.assertEqual(message, "No Discrepancies Found")
	
	def test_one_inequal_discrepancy(self,):
		message = format({"ABC":{"physical":3,"digital":5}})
		expected = "1 Discrepancy Found:\nABC - Records show 5, inventory has 3\n"
		self.assertEqual(message, expected)
		
	def test_two_inequal_discrepancies(self,):
		message = format({"ABC":{"physical":3,"digital":5},"DEF":{"physical":7,"digital":2}})
		expected = "2 Discrepancies Found:\nABC - Records show 5, inventory has 3\nDEF - Records show 2, inventory has 7\n"
		self.assertEqual(message, expected)
		
	def test_three_inequal_discrepancies(self,):
		message = format({"ABC":{"physical":3,"digital":5},"DEF":{"physical":7,"digital":2},"GHI":{"physical":0,"digital":3}})
		expected = "3 Discrepancies Found:\nABC - Records show 5, inventory has 3\nDEF - Records show 2, inventory has 7\nGHI - Records show 3, inventory has 0\n"
		self.assertEqual(message, expected)
		
	def test_one_digital_missing_discrepancy(self,):
		message = format({"ABC":{"physical":3,"digital":None}})
		expected = "1 Discrepancy Found:\nABC - Inventory has 3, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_two_digital_missing_discrepancy(self,):
		message = format({"ABC":{"physical":3,"digital":None},"DEF":{"physical":5,"digital":None}})
		expected = "2 Discrepancies Found:\nABC - Inventory has 3, nothing in the records found\nDEF - Inventory has 5, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_three_digital_missing_discrepancy(self,):
		message = format({"ABC":{"physical":3,"digital":None},"DEF":{"physical":5,"digital":None},"GHI":{"physical":8,"digital":None}})
		expected = "3 Discrepancies Found:\nABC - Inventory has 3, nothing in the records found\nDEF - Inventory has 5, nothing in the records found\nGHI - Inventory has 8, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_one_physical_missing_discrepancy(self,):
		message = format({"ABC":{"physical":None,"digital":4}})
		expected = "1 Discrepancy Found:\nABC - Records show 4, nothing in inventory found\n"
		self.assertEqual(message, expected)
		
	def test_two_physical_missing_discrepancy(self,):
		message = format({"ABC":{"physical":None,"digital":4},"DEF":{"physical":None,"digital":6}})
		expected = "2 Discrepancies Found:\nABC - Records show 4, nothing in inventory found\nDEF - Records show 6, nothing in inventory found\n"
		self.assertEqual(message, expected)
		
	def test_three_physical_missing_discrepancy(self,):
		message = format({"ABC":{"physical":None,"digital":4},"DEF":{"physical":None,"digital":6},"GHI":{"physical":None,"digital":8}})
		expected = "3 Discrepancies Found:\nABC - Records show 4, nothing in inventory found\nDEF - Records show 6, nothing in inventory found\nGHI - Records show 8, nothing in inventory found\n"
		self.assertEqual(message, expected)
	
	def test_one_inequal_and_one_digital_missing_discrepancy(self,):
		message = format({"ABC":{"physical":3,"digital":4},"DEF":{"physical":6,"digital":None}})
		expected = "2 Discrepancies Found:\nABC - Records show 4, inventory has 3\nDEF - Inventory has 6, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_one_inequal_and_one_digital_missing_discrepancy_reversed(self,):
		message = format({"DEF":{"physical":6,"digital":None},"ABC":{"physical":3,"digital":4},})
		expected = "2 Discrepancies Found:\nABC - Records show 4, inventory has 3\nDEF - Inventory has 6, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_one_inequal_and_one_physical_missing_discrepancy(self,):
		message = format({"ABC":{"physical":3,"digital":4},"DEF":{"physical":None,"digital":6}})
		expected = "2 Discrepancies Found:\nABC - Records show 4, inventory has 3\nDEF - Records show 6, nothing in inventory found\n"
		self.assertEqual(message, expected)
		
	def test_one_inequal_and_one_physical_missing_discrepancy_reversed(self,):
		message = format({"DEF":{"physical":None,"digital":6},"ABC":{"physical":3,"digital":4},})
		expected = "2 Discrepancies Found:\nABC - Records show 4, inventory has 3\nDEF - Records show 6, nothing in inventory found\n"
		self.assertEqual(message, expected)
		
	def test_one_physical_missing_and_one_digital_missing_discrepancy(self,):
		message = format({"ABC":{"physical":None,"digital":4},"DEF":{"physical":6,"digital":None}})
		expected = "2 Discrepancies Found:\nABC - Records show 4, nothing in inventory found\nDEF - Inventory has 6, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_one_physical_missing_and_one_digital_missing_discrepancy_reversed(self,):
		message = format({"DEF":{"physical":6,"digital":None},"ABC":{"physical":None,"digital":4}})
		expected = "2 Discrepancies Found:\nABC - Records show 4, nothing in inventory found\nDEF - Inventory has 6, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_one_inequal_and_one_physical_missing_and_one_digital_missing_descrepancy(self,):
		message = format({"DEF":{"physical":6,"digital":None},"GHI":{"physical":8,"digital":7},"ABC":{"physical":None,"digital":4}})
		expected = "3 Discrepancies Found:\nGHI - Records show 7, inventory has 8\nABC - Records show 4, nothing in inventory found\nDEF - Inventory has 6, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_two_inequal_and_two_physical_missing_and_two_digital_missing_descrepancy(self,):
		message = format({"DEF":{"physical":9,"digital":8},"JKL":{"physical":None,"digital":5},"ABC":{"physical":8,"digital":7},"PQR":{"physical":6,"digital":None},"GHI":{"physical":None,"digital":4},"MNO":{"physical":3,"digital":None}})
		expected = "6 Discrepancies Found:\nDEF - Records show 8, inventory has 9\nABC - Records show 7, inventory has 8\nJKL - Records show 5, nothing in inventory found\nGHI - Records show 4, nothing in inventory found\nPQR - Inventory has 6, nothing in the records found\nMNO - Inventory has 3, nothing in the records found\n"
		self.assertEqual(message, expected)
		
	def test_digital_zero_and_physical_missing(self,):
		message = format({"ABC":{"physical":None,"digital":0}})
		self.assertEqual(message, "No Discrepancies Found")
		
	def test_physical_zero_and_digital_missing(self,):
		#the likelyhood of this scenario is slim to none, adding the edge case just in case the code upstream changes
		message = format({"ABC":{"physical":0,"digital":None}})
		self.assertEqual(message, "No Discrepancies Found")
		
	def test_digital_missing_and_physical_missing(self,):
		#again, not likely this will ever happen, but having the edge case covered anyway
		message = format({"ABC":{"physical":None,"digital":None}})
		self.assertEqual(message, "No Discrepancies Found")