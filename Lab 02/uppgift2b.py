def create_shopping_list():
	
	"""
	Creates a new shopping list.
	"""

	return ["Kurslitteratur", "Anteckningsblock", "Penna"]


def shopping_list(slist):
	
	"""
	Lists items currently in shopping list.
	"""

	position = 1
	for i in slist:
		print(str(position) + ". " + i)
		position = position + 1	


def shopping_add(slist):
	"""Adds an item to the shopping list."""
	item_add = input("Vad ska läggas till i listan? (ange endast produktens namn): ")
	slist.append(item_add)


def shopping_remove(slist):
	
	"""
	Removes an item from the shopping list.
	"""

	try:
		item = int(input("Vilken produkt ska plockas bort? (ange dess nummer): "))
		slist.pop(item -1)
	except:
		print("Fel: Produkten måste vara ett numeriskt värde som finns med i listan!")


def shopping_edit(slist):

	"""
	Edits an already existing item on the shopping list.
	"""

	try:
		item = int(input("Vilken produkt vill du redigera? (ange dess nummer): "))
		edit = input("Vad ska stå istället för " + slist[item -1] + "? (ange ett produktnamn): ")
		slist[item -1] = edit
	except:
		print("Fel: Produkten måste vara ett numeriskt värde som finns med i listan!")

		