def format(discrepancies, margins = None):
	if discrepancies == {}:
		return "No Discrepancies Found"
	inequal_messages = ""
	missing_physical_message = ""
	missing_digital_message = ""
	valid_discrepancies = 0
	for item, entry in discrepancies.items():
		valid_discrepancies += 1
		if entry["digital"] == None:
			if entry["physical"] in [0,None]:
				valid_discrepancies -= 1
				continue
			missing_digital_message += "{} - Inventory has {}, nothing in the records found\n".format(item, entry["physical"])
		elif entry["physical"] == None:
			if entry["digital"] in [0,None]:
				valid_discrepancies -= 1
				continue
			missing_physical_message += "{} - Records show {}, nothing in inventory found\n".format(item, entry["digital"])
		else:
			inequal_messages += "{} - Records show {}, inventory has {}\n".format(item, entry["digital"],entry["physical"])
	if valid_discrepancies == 0:
		return "No Discrepancies Found"
	message = "1 Discrepancy Found:\n"
	if len(discrepancies) > 1:
		message = "{} Discrepancies Found:\n".format(valid_discrepancies)
	return message + inequal_messages + missing_physical_message + missing_digital_message