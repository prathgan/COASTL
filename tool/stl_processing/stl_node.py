class Node(object):

	"""
	Constructs node to be used in tree representing expression of signal temporal logical.

    Parameters
    ----------
    parent: 		pointer to the object of parent of this node
    child1: 		pointer to the object of child1; points to anterior requirement of 'until' logic
	child2: 		pointer to the object of child2; points to posterior condition of 'until' logic
    type: 			part of logic which this node represents; logic (0) or predicate (1)
    logic: 			logic operator which which this node represents, null if predicate node
    vars: 			variables which this node pertains to
    range_start: 	start of range for complex operator nodes, min range
    range_end: 		end of range for complex operator nodes, max range
	string_rep: 	string representation of node
    """
	def __init__(self, parent, child1, child2, type, logic, vars, range_start, range_end, string_rep):
		self.__parent = parent
		self.__child1 = child1
        self.__child2 = child2
		self.__type = type
		self.__logic = logic
		self.__vars = vars
		self.__range_start = range_start
		self.__range_end = range_end
		self.__value = ""
		self.__string_rep = string_rep

	@property
	def parent(self):
		"""Return parent"""
		return self.__parent

	@property
	def child1(self):
		"""Return child1"""
		return self.__child1

    @property
	def child2(self):
		"""Return child2"""
		return self.__child2

	@property
	def type(self):
		"""Return type"""
		return self.__type

	@property
	def logic(self):
		"""Return logic"""
		return self.__logic

	@property
	def vars(self):
		"""Return vars"""
		return self.__vars

	@property
	def range_start(self):
		"""Return range_start"""
		return self.__range_start

	@property
	def range_end(self):
		"""Return range_end"""
		return self.__range_end

	@property
	def value(self):
		"""Return string representation of this node"""
		return self.__string_rep

	@parent.setter
	def parent(self, parent):
		"""Set parent"""
		self.__parent = parent
		parent.children = parent.children + [self]

	def set_parent_alt(self,parent):
		"""Set parent without setting child of parent to self"""
		self.__parent = parent

	@children.setter
	def child1(self, children):
		"""Set children"""
		self.__child1 = child1

    @children.setter
	def child2(self, children):
		"""Set children"""
		self.__child2 = child2

	def propogate_var_up(self, var):
		"""Remove all variables except for var until junction node"""
		if len(self.__children)>1:
			return
		self.__vars = var
		self.__parent.propogate_var_up(var)

	def propogate_var_down(self, var, parent, top):
		"""Propogate value of var down children and set parents"""
		self.__vars += "," + var
		if top == 0:
			self.__parent = parent
		if self.__children==None:
			self.propogate_var_up(var)
		for child in self.__children:
			child.propogate_var_down(var, self, 0)

	def get_highest_ancestor(self):
		"""Return highest ancestor"""
		if __parent == None:
			return self
		else:
			return __parent.get_highest_ancestor

	@property
	def value_alt(self):
		"""Complicated return string representation of this node"""
		if self.__type==0:
			if self.__logic=="G" or self.__logic=="F" or self.__logic=="U":
				self.__value = self.__logic+"["+str(self.__range_start)+","+\
				str(self.__range_end)+"]"
			if self.__logic=="~" or self.__logic=="|" or self.__logic=="&":
				self.__value = self.__logic
		elif self.__type==1:
			self.__value = str(self.__vars)+self.__logic+\
			str(self.__range_start if self.__range_start==self.__range_end else\
			self.__range_start if self.__range_end==None else self.__range_end)
		return self.__value

	def __repr__(self, level=0):
		"""Return string representation of this node"""
		ret = "\t"*level+repr(self.value)
		(self.__children)
		for child in self.children:
			ret += "\n" + child.__repr__(level+1)
		return ret
