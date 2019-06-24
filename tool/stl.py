import re
"""
must translate string of logic such as "!G[0,10](F[1,3](!(x>=1)&&(y<=0))" intro tree structure
"""
def process_logic(logic):
	print(logic)
	control_indices = logic_string_breakdown(logic)
	predicate_nodes = process_predicate_nodes(logic, control_indices)
	tree = []
	tree = tree + predicate_nodes
	tree = tree + process_predicate_modifiers(predicate_nodes)
	# should return root of tree
	
# maybe use a FIFO queue to verify all parenthesis are closed

def logic_string_breakdown(str):
	elements = {}
	elements['G'] = [m.start() for m in re.finditer("G", str)]
	elements['F'] = [m.start() for m in re.finditer("F", str)]
	elements['U'] = [m.start() for m in re.finditer("U", str)]
	elements['!'] = [m.start() for m in re.finditer("!", str)]
	elements['||'] = [m.start() for m in re.finditer("||", str)]
	elements['&&'] = [m.start() for m in re.finditer("&&", str)]
	elements['['] = [m.start() for m in re.finditer("\[", str)]
	elements[']'] = [m.start() for m in re.finditer("\]", str)]
	elements['('] = [m.start() for m in re.finditer("\(", str)]
	elements[')'] = [m.start() for m in re.finditer("\)", str)]
	elements[','] = [m.start() for m in re.finditer(",", str)]
	elements['<'] = [m.start() for m in re.finditer("<", str)]
	elements['>'] = [m.start() for m in re.finditer(">", str)]
	elements['='] = [m.start() for m in re.finditer("=", str)]
	return elements

def process_predicate_nodes(logic, control_indices):
	node_array = []
	predicate_operators = control_indices["<"]+control_indices[">"]+control_indices["="]
	predicate_operators.sort()
	this_operator_ind = 0
	for operator in predicate_operators:
		if this_operator_ind < len(predicate_operators)-1 and\
		abs(predicate_operators[this_operator_ind]-\
		predicate_operators[this_operator_ind+1])==1:
			logic_operator_ind = predicate_operators[this_operator_ind]
			left_paren_search_ind = logic_operator_ind-1
			while left_paren_search_ind>=0:
				if(logic[left_paren_search_ind]=="("):
					break
				left_paren_search_ind = left_paren_search_ind-1
			right_paren_search_ind = logic_operator_ind+2
			while right_paren_search_ind<len(logic):
				if(logic[right_paren_search_ind]==")"):
					break
				right_paren_search_ind = right_paren_search_ind+1
			variable = logic[left_paren_search_ind+1:logic_operator_ind]
			minrange = None
			maxrange = None
			if logic[logic_operator_ind]==">":
				minrange = float(logic[logic_operator_ind+2:right_paren_search_ind])
			elif logic[logic_operator_ind]=="<":
				maxrange = float(logic[logic_operator_ind+2:right_paren_search_ind])
			logic_operator = logic[logic_operator_ind:logic_operator_ind+2]
			nodename = "node_"+str(logic_operator_ind)
			exec(nodename+" = Node(None,[],1,logic_operator,variable,minrange,maxrange,\
					[left_paren_search_ind,right_paren_search_ind])")
			exec("node_array.append("+nodename+")")
			this_operator_ind = this_operator_ind+1
		elif this_operator_ind <= len(predicate_operators)-1:
			logic_operator_ind = predicate_operators[this_operator_ind]
			left_paren_search_ind = logic_operator_ind-1
			while left_paren_search_ind>=0:
				if(logic[left_paren_search_ind]=="("):
					break
				left_paren_search_ind = left_paren_search_ind-1
			right_paren_search_ind = logic_operator_ind+1
			while right_paren_search_ind<len(logic):
				if(logic[right_paren_search_ind]==")"):
					break
				right_paren_search_ind = right_paren_search_ind+1
			variable = logic[left_paren_search_ind+1:logic_operator_ind]
			minrange = None
			maxrange = None
			if logic[logic_operator_ind]==">":
				minrange = float(logic[logic_operator_ind+1:right_paren_search_ind])
			elif logic[logic_operator_ind]=="<":
				maxrange = float(logic[logic_operator_ind+1:right_paren_search_ind])
			logic_operator = logic[logic_operator_ind:logic_operator_ind+1]
			nodename = "node_"+str(logic_operator_ind)
			exec(nodename+" = Node(None,[],1,logic_operator,variable,minrange,maxrange,\
				[left_paren_search_ind,right_paren_search_ind])")
			exec("node_array.append("+nodename+")")
		this_operator_ind = this_operator_ind+1
	return node_array

def process_predicate_modifiers(predicate_nodes):
	tree_appendix = []
	pred_arr_index = 0
	for node in predicate_nodes:
		if logic[node.string_bounds[0]-1:node.string_bounds[0]]=="!":
			node.parent = Node(None, [node], 0, "!", node.vars, None, None, [node.string_bounds[0]-1,node.string_bounds[0]-1])
			tree_appendix.append(node.parent)
		if pred_arr_index<len(predicate_nodes)-1\
		and (logic[node.string_bounds[1]+1:predicate_nodes[pred_arr_index+1].string_bounds[0]]=="&&"\
		or logic[node.string_bounds[1]+1:predicate_nodes[pred_arr_index+1].string_bounds[0]]=="||"):
			# print(str(node)+" and "+str(predicate_nodes[pred_arr_index+1])+" have operator between them")
			pass # create parent node to these nodes with operator
		pred_arr_index = pred_arr_index + 1
	return tree_appendix

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
	def __init__(self, parent, children, ttype, logic, vvars, range_start, range_end, string_bounds):
		self.__parent = parent
		self.__children = children
		self.__type = ttype
		self.__logic = logic
		self.__vars = vvars
		self.__range_start = range_start
		self.__range_end = range_end
		self.__value = ""
		self.__string_bounds = string_bounds

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
	def string_bounds(self):
		"""returns range_end"""
		return self.__string_bounds

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

	@children.setter
	def children(self, children):
		self.__children = children

	def __repr__(self, level=0):
		ret = "\t"*level+repr(self.value)
		for child in self.children:
			ret += "\n" + child.__repr__(level+1)
		return ret

