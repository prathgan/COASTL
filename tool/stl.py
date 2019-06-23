import re
"""
must translate string of logic such as "!G[0,10](F[1,3](!(x>=1)&&(y<=0))" intro tree structure
"""
def process_logic(logic):
	control_indices = logic_string_breakdown(logic)
	print(control_indices)

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
	print(str)
	return elements

class Node(object):
	
	"""
	Constructs node to be used in tree representing expression of signal temporal logical.

    Parameters
    ----------
    parent: pointer to the object of parent of this node
    child1: pointer to the object of first child of this node; points to anterior requirement of 'until' logic
    child2: pointer to the object of second child of this ndoe; points to posterior condition of 'until' logic
    ttype: part of logic which this node represents; logic (0) or predicate (1) (ttype not type because type is Python keyword)
    logic: logic operator which which this node represents, null if predicate node
    vvars: variables which this node pertains to (vvars not vars because vars is Python keyword)
    range_start: start of range for complex operator nodes
    range_end: end of range for complex operator nodes

    Raises
    ------
    N/A
    """
	def __init__(self, parent, child1, child2, ttype, logic, vvars, range_start, range_end):
		self.__parent = parent
		self.__child1 = child1
		self.__child2 = child2
		self.__type = ttype
		self.__logic = logic
		self.__vars = variables
		self.__range_start = range_start
		self.__range_end = range_end

	@property
	def parent(self):
		"""returns parent"""
		return self.__parent
		
	@property
	def child1(self):
		"""returns child1"""
		return self.__child1
	
	@property
	def child2(self):
		"""returns child2"""
		return self.__child2

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

