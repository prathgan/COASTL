def display_contract(c):
	"""displays Contract c in a readable manner"""
	print(c)

def display_tree(root):
	"""displays tree with root Node root in a readable manner"""
	print(root)

def list_union(l1,l2):
	return list(set().union(l1,l2))

def join_stringlists(str1, str2):
	"""Return string of union of two sets represented as strings"""
	return ','.join(list_union(str1.split(','),str2.split(',')))
