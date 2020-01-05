import re

def extract_phone(input):
	"""Check firs phone nubmer in input string"""
	phone_regex = re.compile(r'\b\d{2}-?\s?\d{2}-?\s?\d{2}\b') #\b boundaries
	match = phone_regex.search(input)
	if match:
		return match.group()
	else:
		return None

def extract_all_phones(input):
	"""Check all phone nubmers in input string"""
	phone_regex = re.compile(r'\b\d{2}-?\s?\d{2}-?\s?\d{2}\b') #\b boundaries
	match = phone_regex.findall(input)
	return match


def is_valid_phone(input):
	"""check that inpute string is valid phone number"""
	phone_regex = re.compile(r'\d{2}-?\s?\d{2}-?\s?\d{2}') 
	match = phone_regex.fullmatch(input) #fullmatch return match object, without boudaries. Same as findall with boudaries.
	if match:
		return True
	else:
		return False
