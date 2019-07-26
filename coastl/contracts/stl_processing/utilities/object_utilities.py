def display_contract(c):
	"""Display Contract c in a readable manner"""
	print(c)

def display_tree(root):
	"""Display tree with root Node root in a readable manner"""
	print(root)

def display_model(m):
	"""Display all varibles in gurobi model m with their values"""
	for v in m.getVars():
		print('%s %g' % (v.varName, v.x))
