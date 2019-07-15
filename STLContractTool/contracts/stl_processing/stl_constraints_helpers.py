from .utilities.simple_utilities import list_to_str
import re

def get_bin_name(inp):
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
	return name

def replace_operators(str):
	str = str.replace('_p_','+')
	str = str.replace('_m_','-')
	str = str.replace('_t_','*')
	str = str.replace('_d_','/')
	return str

def remove_operators(str):
	str = str.replace('+','')
	str = str.replace('-','')
	str = str.replace('*','')
	str = str.replace('/','')
	return str

def handle_no_range(node):
	if node.range_start==None or node.range_end==None:
		node.range_start = 0
		node.range_end = 0
	return node

def isolate_0(node):
	exp = node.string_rep
	parts = re.split("<=", exp)
	return parts[1]+" - ("+parts[0]+")"


class SwitchDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key)
