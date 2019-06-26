import re

def process(logic):
	return process_logic(logic, 1)

# TODO: when find the variables at the predicate node, propogate the variable up through empty variable fields in logic nodes
def process_logic(logic, root):
	print(logic)
	if logic=="":
		return []
	start,end = round_parens(logic, 0)
	if logic[start+1]=='G' or logic[start+1]=='F':
		firstnum, secondnum, closep = square_parens(logic,start+2)
		if root==1:
			(logic[start+1])
			(logic[closep+1:end])
			return Node(None, process_logic(logic[closep+1:end], 0), 0, logic[start+1], "", firstnum, secondnum)
		else:
			(logic[start+1])
			(logic[closep+1:end])
			return [Node(None, process_logic(logic[closep+1:end],0), 0, logic[start+1], "", firstnum, secondnum)]

	andor_logic, andor_ind = find_andor(logic)
	if andor_logic != None:
		left_start, left_end, right_start, right_end = find_andor_children(logic,andor_ind)
		return Node(None, [process_logic(logic[1:left_end+1],1),process_logic(logic[right_start:len(logic)-1],1)], 0, andor_logic, "", None, None) # error comes from this line
	if logic[start+1]==!:
		return Node(None, process_logic(logic[1:],0), 0, "!", "", None, None)
	predicate_logic, predicate_ind = find_predicate(logic)
	if predicate_logic != None:
		return [Node(None, [], 1, predicate_logic, )] # FINISH
	return []

def round_parens(string, start):
	count = 0
	itr_index = start
	first_not_found = 1
	end = None
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

def round_parens_bwd(string, start):
	count = 0
	itr_index = start
	first_not_found = 1
	end = None
	while itr_index>-1:
		if string[itr_index]==')':
			if first_not_found==1:
				end = itr_index
				first_not_found=0
			count = count + 1
		if string[itr_index]=='(':
			count = count - 1
			if count==0:
				start = itr_index
				break
		itr_index = itr_index - 1
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
	secondnum = float(string[closep-1])
	return firstnum, secondnum, closep

def find_andor(string):
	operator = None
	paren_count = 0
	itr_index = 0
	operator_ind = -1
	while itr_index<len(string):
		if string[itr_index]=='(':
			paren_count = paren_count + 1
		if string[itr_index]==')':
			paren_count = paren_count - 1
		if paren_count==1 and (string[itr_index]=="&" or string[itr_index]=="|"):
			operator_ind = itr_index
			operator = string[itr_index:itr_index+2]
			return operator, operator_ind
		itr_index = itr_index + 1
	return operator, operator_ind

def find_andor_children(string, andor_ind):
	right_start, right_end = round_parens(string,andor_ind+2)
	left_start, left_end = round_parens_bwd(string,andor_ind-1)
	return left_start, left_end, right_start, right_end

def find_predicate(string):
	operator = None
	paren_count = 0
	itr_index = 0
	operator_ind = -1
	while itr_index<len(string):
		if string[itr_index]=='(':
			paren_count = paren_count + 1
		if string[itr_index]==')':
			paren_count = paren_count - 1
		if paren_count==1 and (string[itr_index]=="<" or string[itr_index]==">" or string[itr_index]=="="):
			operator_ind = itr_index
			if string[itr_index+1]=="=":
				operator = string[itr_index:itr_index+2]
			else:
				operator = string[itr_index]
			return operator, operator_ind
		itr_index = itr_index + 1
	return operator, operator_ind

def find_predicate_info(string, operator_ind, operator):
	var = find_predicate_var(string, operator_ind)
	minval = None
	maxval = None
	if operator=="<=":
		maxval = find_predicate_num(string)
	elif operator==">=":
		pass
	elif operator=="<":
		pass
	elif operator==">":
		pass
	elif operator=="=":
		pass



def find_predicate_num(string, last_operator_ind):
	itr_index = last_operator_ind
	while itr_index<len(string):
		if string[itr_index]==")":
			return float(string[last_operator_ind+1:itr_index])
		itr_index = itr_index = 1
	return -1

def find_predicate_var(string, operator_ind):
	itr_index = operator_ind
	while itr_index>-1:
		if string[itr_index]=="(":
			return string[itr_index+1:operator_ind]
		itr_index = itr_index - 1
	return -1

class Node(object):

	"""
	Constructs node to be used in tree representing expression of signal temporal logical.

    Parameters
    ----------
    parent: 		pointer to the object of parent of this node
    children: 		array with pointers to the objects of children of this node; children[0]
    		  		points to anterior requirement of 'until' logic, children[1] points to
    		  		posterior condition of 'until' logic
    ttype: 			part of logic which this node represents; logic (0) or predicate (1) (ttype not
    	   			type because type is Python keyword)
    logic: 			logic operator which which this node represents, null if predicate node
    vvars: 			variables which this node pertains to (vvars not vars because vars is Python keyword)
    range_start: 	start of range for complex operator nodes, min range
    range_end: 		end of range for complex operator nodes, max range
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
		(self.__children)
		for child in self.children:
			ret += "\n" + child.__repr__(level+1)
		return ret
