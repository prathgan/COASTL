import re

"""
must translate string of logic such as "!G[0,10](F[1,3](!(x>=1)&&(y<=0))" intro tree structure
"""

# when find the variables at the predicate node, propogate the variable up through empty variable fields in logic nodes
# recursively break down string into tree
def process_logic(logic):
	if logic=="":
		return []
	if logic[0]:
		pass
	if logic[0]=='G' or logic[0]=='F':
		firstnum, secondnum, closep = square_parens(logic,1)
		return Node(None, process_logic(logic[closep+1:len(logic)]), 0, logic[0], "", firstnum, secondnum)


		

def round_parens(string, start):
	count = 0
	itr_index = start
	first_not_found = 1
	openp = 0
	closep = 0
	while itr_index<len(string):
		if string[itr_index]=='(':
			if first_not_found==1:
				start = itr_index
				first_not_found=0
			count = count + 1
		if string[itr_index]==')':
			count = count - 1
			if count==0:
				end = itr_index
				break
		itr_index = itr_index + 1
	return start, end

def square_parens(string, start):
	itr_index = start
	comma = 0
	closep = 0
	while itr_index<len(string):
		if string[itr_index]==',':
			comma = itr_index
		if string[itr_index]==']':
			closep = itr_index
			break
		itr_index = itr_index + 1
	firstnum = float(string[start+1:comma])
	secondnum = float(string[comma+1:len(string)-1])
	return firstnum, secondnum, closep

class Node(object):
	
	"""
	Constructs node to be used in tree representing expression of signal temporal logical.

    Parameters
    ----------
    parent: pointer to the object of parent of this node
    children: array with pointers to the objects of children of this node; children[0] 
    		  points to anterior requirement of 'until' logic, children[1] points to 
    		  posterior condition of 'until' logic
    ttype: part of logic which this node represents; logic (0) or predicate (1) (ttype not 
    	   type because type is Python keyword)
    logic: logic operator which which this node represents, null if predicate node
    vvars: variables which this node pertains to (vvars not vars because vars is Python keyword)
    range_start: start of range for complex operator nodes, min range
    range_end: end of range for complex operator nodes, max range

    Raises
    ------
    N/A
    """
	def __init__(self, parent, children, ttype, logic, vvars, range_start, range_end):
		self.__parent = parent
		self.__children = children
		self.__type = ttype
		self.__logic = logic
		self.__vars = vvars
		self.__range_start = range_start
		self.__range_end = range_end
		self.__value = ""

	@property
	def parent(self):
		"""returns parent"""
		return self.__parent
		
	@property
	def children(self):
		"""returns child1"""
		return self.__children

	@property
	def type(self):
		"""returns self"""
		return self.__type

	@property
	def logic(self):
		"""returns logic"""
		return self.__logic
	
	@property
	def vars(self):
		"""returns vars"""
		return self.__vars
	
	@property
	def range_start(self):
		"""returns range_start"""
		return self.__range_start

	@property
	def range_end(self):
		"""returns range_end"""
		return self.__range_end

	@property
	def value(self):
		"""returns string representation of this node"""
		if self.__type==0:
			if self.__logic=="G" or self.__logic=="F" or self.__logic=="U":
				self.__value = self.__logic+"["+str(self.__range_start)+","+\
				str(self.__range_end)+"]"
			if self.__logic=="!" or self.__logic=="||" or self.__logic=="&&":
				self.__value = self.__logic
		elif self.__type==1:
			self.__value = str(self.__vars[0])+self.__logic+\
			str(self.__range_start if self.__range_start==self.__range_end else\
			self.__range_start if self.__range_end==None else self.__range_end)
		return self.__value

	@parent.setter
	def parent(self, parent):
		self.__parent = parent
		parent.children = parent.children + [self]

	@children.setter
	def children(self, children):
		self.__children = children

	def get_highest_ancestor(self):
		if __parent == None:
			return self
		else:
			return __parent.get_highest_ancestor

	def __repr__(self, level=0):
		ret = "\t"*level+repr(self.value)
		for child in self.children:
			ret += "\n" + child.__repr__(level+1)
		return ret

