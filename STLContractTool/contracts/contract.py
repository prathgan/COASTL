from .stl_processing.stl_node import Node
from .stl_processing.stl_processing import parse_stl, synthesize_stl
from .stl_processing.utilities.simple_utilities import join_stringlists, remove_dups_stringlist, list_to_str

class Contract(object):
	"""docstring for Contract"""
	def __init__(self, variables, assumptions, guarantees):
		if isinstance(assumptions, Node):
			self.__assumptions = assumptions
		else:
			self.__assumptions = parse_stl(assumptions)
		if isinstance(guarantees, Node):
			self.__guarantees = guarantees
		else:
			self.__guarantees = parse_stl(guarantees)
		self.process_variables(variables)
		self.__isSat = 0

	def process_assumptions(self, assumptions):
		self.__assumptions = parse_stl(assumptions)

	def process_guarantees(self, guarantees):
		self.__guarantees = parse_stl(guarantees)

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

	@property
	def isSat(self):
		return self.__isSat

	def saturate(self):
		notA = Node(None, self.__assumptions, None, 0, "~", self.__assumptions.vars, None, None, "~")
		self.__guarantees = Node(None, notA, self.__guarantees, 0, "||", join_stringlists(notA.vars,self.__guarantees.vars), None, None, "||")
		notA.set_parent_alt("self.__guarantees")
		self.__isSat = 1

	def __repr__(self):
		return "Variables:\n"+list_to_str(self.__variables)+"\nAssumptions:\n"+str(self.__assumptions)+"\nGuarantees:\n"+str(self.__guarantees)
