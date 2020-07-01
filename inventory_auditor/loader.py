class Loader:
	def __init__(self,):
		self.products = {}
	def get_file_type(self,):
		return "default"
	def load(self, file):
		return {}
	def _enter_product(self, product, quantity):
		if type(quantity) != int or type(product) != str:
			raise TypeError()
		if product not in self.products:
			self.products[product] = quantity
		else:
			self.products[product] += quantity