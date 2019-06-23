def display(c):
	"""displays Contract c in a readable manner"""
	print("Variables:")
	print(c.variables)
	print("Assumptions:")
	print(c.assumptions)
	print("Guarantees:")
	print(c.guarantees)