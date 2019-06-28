from stl import Node
from stl import process
from operations import list_union

class Contract(object):
	"""docstring for Contract"""
	def __init__(self, variables, assumptions, guarantees):
		self.process_assumptions(assumptions)
		self.process_guarantees(guarantees)
		self.process_variables(variables)
		self.__isSat = 0

	def process_assumptions(self, assumptions):
		assum_arr = []
		for assumption in assumptions:
			assum_arr.append(process(assumption))
		self.__assumptions = assum_arr

	def process_guarantees(self, guarantees):
		guar_arr = []
		for guarantee in guarantees:
			guar_arr.append(process(guarantee))
		self.__guarantees = guar_arr

	def process_variables(self, variables):
		for var in variables:
			self.__assumptions.propogate_var_down(var, None, 1)
			self.__guarantees.propogate_var_down(var, None, 1)
		self.__variables = variables

	@property
	def variables(self):
		return self.__variables

	@property
	def assumptions(self):
		return self.__assumptions

	@property
	def guarantees(self):
		return self.__guarantees

	def saturate(self):
		notA = Node(None, self.__assumptions, 0, "!", self.__assumptions.vars, None, None, "!")
		self.__guarantees = Node(None, [notA,self.guarantees], 0, "||", ','.join(list_union(notA.vars.split(','),self.guarantees.vars.split(','))), None, None, "||")
		notA.parent = self.__guarantees
		self.__isSat = 1

	def __repr__(self):
		print("Variables:")
		print(self.__variables)
		print("Assumptions:")
		print(self.__assumptions)
		print("Guarantees:")
		print(self.__guarantees)
