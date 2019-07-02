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

def list_to_str(l):
	return ','.join(l)
