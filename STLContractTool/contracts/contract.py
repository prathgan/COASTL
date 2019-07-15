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
		self.__model = None

	def process_assumptions(self, assumptions):
		self.__assumptions = parse_stl(assumptions)

	def process_guarantees(self, guarantees):
		self.__guarantees = parse_stl(guarantees)

	def process_variables(self, variables):
		for var in variables:
			if self.__assumptions is not "T":
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

	@property
	def model(self):
		return self.__model

	def saturate(self):
		if self.__assumptions == "T":
			self.__isSat == 1
			return
		notA = Node(None, self.__assumptions, None, 0, "~", self.__assumptions.vars, None, None, "~")
		self.__guarantees = Node(None, notA, self.__guarantees, 0, "||", join_stringlists(notA.vars,self.__guarantees.vars), None, None, "||")
		notA.set_parent_alt(self.__guarantees)
		self.__isSat = 1

	def __repr__(self):
		return "Variables:\n"+list_to_str(self.__variables)+"\nAssumptions:\n"+str(self.__assumptions)+"\nGuarantees:\n"+str(self.__guarantees)

	def synthesize(self, ret_type=0, remove_log=False, console_log=True, maximize_vars=None, minimize_vars=None):
		if self.__isSat == 0:
			self.saturate()
		self.__model = synthesize_stl(self.guarantees, ret_type, remove_log, console_log, maximize_vars, minimize_vars)

	def get_synthesized_vars(self):
		vars = {}
		for var in self.__model.getVars():
			if var.VarName.split("_")[0] in self.__variables:
				vars.update({var.VarName:var.x})
		return vars
