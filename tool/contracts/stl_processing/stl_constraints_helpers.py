from sympy import *

def get_bin_name(node):
	name = "b_"+node.string_rep
	name = name.replace('[','_')
	name = name.replace(']','_')
	name = name.replace(',','_')
	name = name.replace("<=",'leq')
	name = name.replace(">=",'geq')
	name = name.replace('<','l')
	name = name.replace('>','g')
	name = name.replace("&&","and")
	name = name.replace('||',"or")
	name = name.replace('~',"not")
	return name

def handle_no_range(node):
	if node.range_start==None or node.range_end==None:
		node.range_start = 0
		node.range_end = 0
	return node

def isolate_0(expr):


class SwitchDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key)
