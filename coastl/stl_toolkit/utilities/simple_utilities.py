import os

def list_union(l1,l2):
	"""Return union of elements in two lists"""
	return list(set().union(l1,l2))

def join_stringlists(str1, str2):
	"""Return string of union of two sets represented as strings"""
	return ','.join(list_union(str1.split(','),str2.split(',')))

def remove_dups_stringlist(str):
	"""Remove duplicates from list as string"""
	arr = str.split(',')
	arr = list(dict.fromkeys(arr))
	return ','.join(arr)

def list_to_str(l, commas=True):
	"""Converts list to string representation"""
	if commas:
		return ','.join(l)
	else:
		return ''.join(l)

def parentheses_match(string):
	"""
	Return True if opening and closing brackets are
	all matched in an input logical expression
	"""
	verification_stack = []
	matched = True
	itr_index = 0
	while itr_index < len(string) and matched:
		if string[itr_index]=="(":
			verification_stack.append(string[itr_index])
		elif string[itr_index]==")":
			if len(verification_stack)==0:
				matched = False
			else:
				verification_stack.pop()
		itr_index += 1
	return matched and len(verification_stack) == 0

def remove_gurobi_log():
	"""Removes gurobi log after COASTL synthesis function has been run"""
	os.remove("gurobi.log")
