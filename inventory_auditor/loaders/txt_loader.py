from inventory_auditor.loader import Loader
class TxtLoader(Loader):
	def get_file_type(self,):
		return "txt"
	def load(self, file):
		self.products = {}
		with open(file) as f:
			for line in f.readlines():
				product = line.split(' ')[0]
				quantity = line.split(' ')[1]
				self._enter_product(product, int(quantity))
		return self.products