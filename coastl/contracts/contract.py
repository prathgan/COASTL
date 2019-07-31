import sys
sys.path.insert(1,'../stl_toolkit')
from .stl_processing.stl_node import Node
from .stl_processing.stl_processing import parse_stl, synthesize_stl
from .stl_processing.utilities.simple_utilities import join_stringlists, remove_dups_stringlist, list_to_str

class Contract(object):
	def __init__(self, variables, assumptions, guarantees):
		"""
		Constructs Contract object with specified logics

	    Parameters
	    ----------
	    variables: 		variables reasoned about in A & G, format: ['x','y']
	    assumptions: 	assumptions of contract, written as STL, format: "G[0,1](x<=2)"
		guarantees: 	guarantees of contract, written as STL, format: "G[0,1](x<=2)"
	    """
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
		"""Set assumptions to STL tree of assumptions"""
		self.__assumptions = parse_stl(assumptions)

	def process_guarantees(self, guarantees):
		"""Set guarantees to STL tree of guarantees"""
		self.__guarantees = parse_stl(guarantees)

	def process_variables(self, variables):
		"""Propogate variables down nodes of STL trees of A & G"""
		for var in variables:
			if self.__assumptions is not "T":
				self.__assumptions.propogate_var_down(var, None, 1)
			self.__guarantees.propogate_var_down(var, None, 1)
		self.__variables = variables

	@property
	def variables(self):
		"""Get variables"""
		return self.__variables

	@property
	def assumptions(self):
		"""Get assumptions"""
		return self.__assumptions

	@property
	def guarantees(self):
		"""Get guarantees"""
		return self.__guarantees

	@property
	def isSat(self):
		"""Get saturation"""
		return self.__isSat

	@property
	def model(self):
		"""Get optimization model"""
		return self.__model

	def saturate(self):
		"""Saturate contract"""
		if self.__assumptions == "T":
			self.__isSat == 1
			return
		notA = Node(None, self.__assumptions, None, 0, "~", self.__assumptions.vars, None, None, "~")
		self.__guarantees = Node(None, notA, self.__guarantees, 0, "||", join_stringlists(notA.vars,self.__guarantees.vars), None, None, "||")
		notA.set_parent_alt(self.__guarantees)
		self.__isSat = 1

	def __repr__(self):
		"""Get string representation of contract, used in print(contract)"""
		return "Variables:\n"+list_to_str(self.__variables)+"\nAssumptions:\n"+str(self.__assumptions)+"\nGuarantees:\n"+str(self.__guarantees)

	def synthesize(self, ret_type=0, remove_log=False, console_log=True, maximize_vars=None, minimize_vars=None):
		"""Synthesize values for continuous variables in A & G, optimize model"""
		if self.__isSat == 0:
			self.saturate()
		self.__model = synthesize_stl(self.guarantees, ret_type, remove_log, console_log, maximize_vars, minimize_vars)

	def get_synthesized_vars(self):
		"""Get dict in format {var1: x1, var2: x2}"""
		vars = {}
		for var in self.__model.getVars():
			if var.VarName.split("_")[0] in self.__variables:
				vars.update({var.VarName:var.x})
		return vars
