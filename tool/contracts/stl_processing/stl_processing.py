import re
from gurobipy import *
from .stl_helper_funcs import *
from .stl_helper_structures import SwitchDict
from .stl_node import Node
from .utilities.simple_utilities import remove_gurobi_log

def process(logic, remove_log=False):
	"""
	Return result of passing logic expression into process_logic()
	"""
	if not parentheses_match(logic):
		raise ValueError("Opening and closing brackets do not match, check '(' and ')'")
	m = Model("optimization_model")
	tree = process_logic(logic, None, None, m)
	if remove_log:
		remove_gurobi_log()
	return tree

def process_logic(logic, range_start, range_end, m):
	"""
	Return root of tree structure which represents
	a Signal Temporal Logic expression
	"""
	if logic=="":
		return None
	start, end = round_parens(logic)
	if start==0 and end==len(logic)-1:
		return process_logic(logic[1:len(logic)-1], range_start, range_end, m)
	node_switch_0 = SwitchDict([("~",not_node),("G",g_node),("F",f_node)])
	if node_switch_0[logic[0]] != None:
		return node_switch_0[logic[0]](logic, start, end, range_start, range_end, m)
	con_info = connector(logic)
	if con_info != -1:
		return con_node(con_info, range_start, range_end, m)
	AP_info = predicate(logic, start, end)
	if AP_info != -1:
		return AP_node(AP_info, logic, range_start, range_end, m)

def not_node(logic, start, end, range_start, range_end, m):
	return Node(None, process_logic(logic[start+1:end, range_start, range_end], range_start, range_end, m), None, 0, "~", "", None, None, "~")

def g_node(logic, start, end, range_start, range_end, m):
	firstnum, secondnum, closep = square_parens(logic, 1)
	return Node(None, process_logic(logic[closep+1:], firstnum, secondnum, m), None, 0, "G", "", None, None, logic[0:closep+1])

def f_node(logic, start, end, range_start, range_end, m):
	firstnum, secondnum, closep = square_parens(logic, 1)
	return Node(None, process_logic(logic[closep+1:], firstnum, secondnum, m), None, 0, "F", "", firstnum, secondnum, logic[0:closep+1])

def con_node(andor_info, range_start, range_end, m):
	return Node(None, process_logic(andor_info[0], range_start, range_end, m), process_logic(andor_info[2], range_start, range_end, m), 0, andor_info[1], "", None, None, andor_info[1])

def AP_node(AP_info,logic, range_start, range_end, m):
	return Node(None, None, None, 1, AP_info[1], AP_info[0], range_start, range_end, logic)
