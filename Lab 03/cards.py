import random

joker_a = 'joker A'
joker_b = 'joker B'
seed = '787'

def create_deck():
	"""Creates a new deck"""
	suits = [1,2]
	values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	deck = []
	for suit in suits: 
		for value in values: 
			deck.append([suit,value,int(len(deck) + 1)]) 
	
	insert_joker(joker_a, deck)
	insert_joker(joker_b, deck)
	
	return deck

def insert_joker(name, deck):
	"""Function for inserting jokers to the end of a deck""" 
	deck.append([name, 27, int(len(deck) + 1)]) 

def get_value_of_card(deck, position, variable):
	"""
	Gets value of specified card. deck is name of the deck. 
	Position is position of the card you want information about.
	Variable can be 'color', 'value' or 'unique_id'.
	"""
	if variable == "color":
		variable_val = 0
		if deck[position][variable_val] == 1:
			return "red"
		else:
			return "black"
	if variable == "value":
		variable_val = 1
		return deck[position][variable_val]
	if variable == "unique_id":
		variable_val = 2
		return deck[position][variable_val]
	else:
		print("Plese enter a valid string: 'color', 'value' or 'unique_id'")

def shuffle_deck(deck): 
	"""Shuffles deck according to seed specified previously."""
	random.seed(seed)
	deck = random.shuffle(deck)

def move_card(old_position, new_position, deck):
	"""Moves a card from a specified position to a new specified position."""
	deck.insert(new_position, deck.pop(old_position))

def split_deck(start_position, end_position, deck):
	"""Splits deck into specified size."""
	return deck[start_position:end_position]

def find_joker_a(deck):
	"""Finds joker A in the specified deck"""
	lst = []
	for position, i in enumerate(deck): 
		if i[0] == joker_a:
			lst.append(position)
	return lst

def find_joker_b(deck):
	"""Finds joker B in the specified deck"""
	lst = []
	for position, i in enumerate(deck): 
		if i[0] == joker_b:
			lst.append(position)
	return lst

def find_jokers(deck):
	"""Finds the jokers in the specified deck"""
	lst = []
	for position, i in enumerate(deck): 
		if i[0] == joker_a or i[0] == joker_b:
			lst.append(position)
	return lst

def move_joker_a(deck): 
	"""Moves joker A according to specified pattern."""
	joker_loc_a = find_joker_a(deck)
	
	if joker_loc_a[0] == (len(deck)-1):     
		move_card(joker_loc_a[0], 1, deck)
	else:
		move_card(joker_loc_a[0], ((joker_loc_a[0]) + 1), deck)

def move_joker_b(deck):
	"""Moves joker B according to specified pattern."""

	joker_loc_b = find_joker_b(deck)
	
	if joker_loc_b[0] == (len(deck)-1):
		move_card(joker_loc_b[0], 2, deck)
	if joker_loc_b[0] == (len(deck)-2):
		move_card(joker_loc_b[0], 1, deck)
	else:
		move_card(joker_loc_b[0], ((joker_loc_b[0]) + 2), deck)


def solitare_keystream(length, deck):
	"""Creates our encryption key."""
	new_deck = deck.copy() # Create new deck that is copy of specified deck.
	shuffle_deck(new_deck) # Shuffle the new deck.
	move_joker_a(new_deck) # Move joker A.
	move_joker_b(new_deck)# Move joker B.
	keychain = [] # Create Empty list
	while len(keychain) < length: # Loop as long as our keychain is less than specified length.
		jokers_loc = find_jokers(new_deck) # Create new list with joker locations.
		deck_a = split_deck(0, jokers_loc[0], deck) # From 0 to the first joker.
		deck_b = split_deck(jokers_loc[0], int(jokers_loc[1] + 1), new_deck) # From the first joker to the last joker.
		deck_c = split_deck(jokers_loc[1] + 1, int(len(new_deck) - 1), new_deck) # From the last joker to the end.
		deck = deck_c + deck_b + deck_a # Move around parts as given in instructions.
		value_of_last_card = get_value_of_card(new_deck, int(len(new_deck)-1), "value") # Get value of last card
		deck_a = split_deck(0, value_of_last_card, new_deck) # From position 0 to the value of the last card.
		deck_b = split_deck(value_of_last_card, int(len(new_deck)-1), new_deck) # From the value of the last card to length of deck. 
		new_deck = deck_b + deck_a # Move around parts as given in instructions.

		index_of_card = get_value_of_card(new_deck, 0, "value")          # Determine value of first card.

		if index_of_card <= 26: # If the value is less than or equal to 26 append to keychanin. (27 is joker so don't append)
			if get_value_of_card(new_deck, index_of_card, "value") <= 26:
				keychain.append(get_value_of_card(new_deck, index_of_card, "value"))

	return keychain 

def convert_char_to_number(char): 
	"""Converts characters to numbers."""
	return int(ord(char) - 64) # A = 1 

def convert_number_to_char(number):
	"""Converts numbers to characters."""
	return chr(number + 64)  # 1 = A 

def convert_string_to_numbers(string):
	"""Converts a string to numbers by using convert_char_to_number."""
	temp = []
	for char in string: 
		temp.append(convert_char_to_number(char))
	return temp

def sum_of(list_1, list_2):
	"""For every value in list_1 loop through and add with value from list_2. If < 26 subtract 26"""
	temp = []
	for i in range(len(list_1)):
		value = list_1[i] + list_2[i]
		if value <= 26:
			temp.append(value)
		else: 
			temp.append(value - 26)
	return temp 

def diff_of(list_1, list_2):
	"""For every value in list_2 loop through and subtract with value from list_1. If value is negative add 26"""
	temp = []
	for i in range(len(list_1)):
		value = list_2[i] - list_1[i]
		if value >= 0:
			temp.append(value)
		else:
			temp.append(value + 26)

	return temp


def solitare_encrypt(message, deck):
	"""Encrypts our message with our keystream from solitare_keystream."""
	message = message.upper()

	key_in_numbers = solitare_keystream(len(message), deck)
	message_in_numbers = convert_string_to_numbers(message)
	crypt_in_numbers = sum_of(key_in_numbers, message_in_numbers)
	crypt_in_letters = []

	for i in crypt_in_numbers:
		crypt_in_letters.append(convert_number_to_char(i))

	return "".join(crypt_in_letters)

def solitare_decrypt(message, deck):
	"""Decrypts our message with our keystream from solitare_keystream."""
	key_in_numbers = solitare_keystream(len(message), deck)
	message_in_numbers = convert_string_to_numbers(message)
	crypt_in_numbers = diff_of(key_in_numbers, message_in_numbers)

	message = []
	for i in crypt_in_numbers:
		message.append(convert_number_to_char(i))  

	return "".join(message) 

def main():
	"""Runs a demonstration of this program."""
	deck = create_deck()
	orig_message = str(input("Enter message you want encrypted: "))
	secret_message = str(solitare_encrypt(orig_message, deck))
	print('\n'"The encrypted message is: ")
	print(secret_message + '\n')
	print("The encryption key: ")
	print(solitare_keystream(len(secret_message), deck))
	print('\n'"Decrypted message is: ")
	print(str(solitare_decrypt(secret_message, deck)))

if __name__ == '__main__':
	main()