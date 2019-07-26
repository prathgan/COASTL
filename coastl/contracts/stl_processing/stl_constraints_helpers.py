from .utilities.simple_utilities import list_to_str
import re

def get_bin_name(inp):
	"""Returns corrected name of binary variable for an stl_node, removes disruptive chars"""
	alphaDict = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
	name = ""
	if isinstance(inp, str):
		name = inp
	else:
		name = "b_"+inp.string_rep
	name = name.replace('[','ob')
	name = name.replace(']','cb')
	name = name.replace(',','_')
	name = name.replace("<=",'leq')
	name = name.replace(">=",'geq')
	name = name.replace('<','l')
	name = name.replace('>','g')
	name = name.replace("&&","and")
	name = name.replace('||',"or")
	name = name.replace('~',"not")
	name = name.replace('(',"_op_")
	name = name.replace(')',"_cp_")
	name = name.replace('+',"_p_")
	name = name.replace('-',"_m_")
	name = name.replace('*',"_t_")
	name = name.replace('/',"_d_")
	name = name.replace('.',"_dot_")
	if name[0].isdigit():
		name=alphaDict[name[0]]+"_"+name[1:]
	return name

def replace_operators(str):
	"""Returns string with mathematical operators put back"""
	str = str.replace('_p_','+')
	str = str.replace('_m_','-')
	str = str.replace('_t_','*')
	str = str.replace('_d_','/')
	return str

def remove_operators(str):
	"""Returns string with mathematical operators removed"""
	str = str.replace('+','')
	str = str.replace('-','')
	str = str.replace('*','')
	str = str.replace('/','')
	return str

def handle_no_range(node):
	"""Returns stl_node with range set to [0,0] if not previously set"""
	if node.range_start==None or node.range_end==None:
		node.range_start = 0
		node.range_end = 0
	return node

def isolate_0(node):
	"""Returns string s where 0<s is found from some expression n<k"""
	exp = node.string_rep
	parts = re.split("<=", exp)
	if exp[-1].isalpha():
		return parts[0]+" - ("+parts[1]+")"
	else:
		return parts[1]+" - ("+parts[0]+")"


class SwitchDict(dict):
	"""Dictionary subclass with dict.get(x), where x is not in dict, returning None"""
    def __getitem__(self, key):
        return dict.get(self, key)
