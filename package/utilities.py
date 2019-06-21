def display(c):
	"""prints contract c represented"""
	print("Variables:")
	print(c.variables)
	print("Assumptions:")
	print(c.assumptions)
	print("Guarantees:")
	print(c.guarantees)