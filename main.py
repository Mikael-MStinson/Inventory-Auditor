from bulk_import import import_subclasses
from inventory_auditor.loader import Loader
loader_classes = import_subclasses(base_class = Loader, directory = "inventory_auditor.loaders")
loaders = {}
for loader in loader_classes:
    loader_object = loader()
    loaders[loader_object.get_file_type()] = loader_object


from argparse import ArgumentParser

parser = ArgumentParser(description = 'Compare an inventory list to a record and return a list of discrepancies')
parser.add_argument('inventory', help='a list of part numbers and their quantities found in storage')
parser.add_argument('record',    help='a list of part numbers and their quantities found in the records')

args = parser.parse_args()

inventory = args.inventory
record = args.record
prompt = '''
inventory ---> {}
record ------> {}

is this correct?
'''
while True:
	print(prompt.format(inventory,record))
	answer = input('y/n > ')
	if answer == 'y':
		break
	elif answer == 'n':
		inventory, record = record, inventory
	else:
		print("invalid response")
print()
		
from inventory_auditor.compare_lists import compare
from inventory_auditor.format_discrepancies import format
inventory_loader = loaders[inventory.split('.')[-1]]
record_loader = loaders[record.split('.')[-1]]
print(format(compare(inventory_loader.load(inventory),record_loader.load(record))))
input("Press Enter to Continue...")