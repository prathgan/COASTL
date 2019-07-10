from .stl_parsing_helpers import *
from .stl_helper_structures import SwitchDict
from .stl_node import Node

def parse(logic):
	return parse_logic(logic, None, None)

def parse_logic(logic, range_start, range_end):
	"""
	Return root of tree structure which represents
	a Signal Temporal Logic expression
	"""
	if logic=="":
		return None
	start, end = round_parens(logic)
	if start==0 and end==len(logic)-1:
		return parse_logic(logic[1:len(logic)-1], range_start, range_end)
	node_switch_0 = SwitchDict([("~",not_node),("G",g_node),("F",f_node)])
	if node_switch_0[logic[0]] != None:
		return node_switch_0[logic[0]](logic, start, end, range_start, range_end)
	con_info = connector(logic)
	if con_info != -1:
		return con_node(con_info, range_start, range_end)
	AP_info = predicate(logic, start, end)
	if AP_info != -1:
		return AP_node(AP_info, logic, range_start, range_end)

def not_node(logic, start, end, range_start, range_end):
	return Node(None, parse_logic(logic[start+1:end], range_start, range_end), None, 0, "~", "", None, None, "~")

def g_node(logic, start, end, range_start, range_end):
	firstnum, secondnum, closep = square_parens(logic, 1)
	return Node(None, parse_logic(logic[closep+1:], firstnum, secondnum), None, 0, "G", "", None, None, logic[0:closep+1])

def f_node(logic, start, end, range_start, range_end):
	firstnum, secondnum, closep = square_parens(logic, 1)
	return Node(None, parse_logic(logic[closep+1:], firstnum, secondnum), None, 0, "F", "", firstnum, secondnum, logic[0:closep+1])

def con_node(andor_info, range_start, range_end):
	return Node(None, parse_logic(andor_info[0], range_start, range_end), parse_logic(andor_info[2], range_start, range_end), 0, andor_info[1], "", None, None, andor_info[1])

def AP_node(AP_info,logic, range_start, range_end):
	return Node(None, None, None, 1, AP_info[1], AP_info[0], range_start, range_end, logic)
