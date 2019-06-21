class Contract(object):
	"""docstring for Contract"""
	def __init__(self, variables, assumptions, guarantees):
		self.process_variables(variables)
		self.process_assumptions(assumptions)
		self.process_guarantees(guarantees)

	def process_variables(self, variables):
		self.__variables = variables

	def process_assumptions(self, assumptions):
		self.__assumptions = assumptions

	def process_guarantees(self, guarantees):
		self.__guarantees = guarantees

	@property
	def variables(self):
		return self.__variables

	@property
	def assumptions(self):
		return self.__assumptions

	@property
	def guarantees(self):
		return self.__guarantees