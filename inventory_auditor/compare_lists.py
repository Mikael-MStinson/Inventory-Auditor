def compare(physical_inventory, digital_inventory):
	if physical_inventory == digital_inventory:
		return {}
	discrepencies = {}
	for item, quantity in digital_inventory.items():
		if item not in physical_inventory:
			discrepencies[item] = {"physical":None,"digital":quantity}
	for item, quantity in physical_inventory.items():
		if item not in digital_inventory:
			discrepencies[item] = {"physical":quantity,"digital":None}
		elif digital_inventory[item] != quantity:
			discrepencies[item] = {"physical":quantity,"digital":digital_inventory[item]}
	return discrepencies