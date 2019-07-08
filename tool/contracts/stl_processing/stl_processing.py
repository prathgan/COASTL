import re
from .stl_helper_funcs import *
from .stl_helper_structures import SwitchDict
from .stl_node import Node

def process(logic):
	"""
	Return result of passing logic expression into process_logic()
	"""
	if not parentheses_match(logic):
		raise ValueError("Opening and closing brackets do not match, check '(' and ')'")
	return process_logic(logic)

def process_logic(logic):
	"""
	Return root of tree structure which represents
	a Signal Temporal Logic expression
	"""
	if logic=="":
		return None
	start, end = round_parens(logic)
	if start==0 and end==len(logic)-1:
		return process_logic(logic[1:len(logic)-1])
	node_switch_0 = SwitchDict([("~",not_node),("G",g_node),("F",f_node)])
	if node_switch_0[logic[0]] != None:
		return node_switch_0[logic[0]](logic, start, end)
	andor_info = andor(logic)
	if andor_info != -1:
		return andor_node(andor_info)
	AP_info = predicate(logic, start, end)
	if AP_info != -1:
		return AP_node(AP_info, logic)

def not_node(logic, start, end):
	return Node(None, process_logic(logic[start+1:end]), None, 0, "~", "", None, None, "~")

def g_node(logic, start, end):
	firstnum, secondnum, closep = square_parens(logic, 1)
	return Node(None, process_logic(logic[closep+1:]), None, 0, "G", "", firstnum, secondnum, logic[0:closep+1])

def f_node(logic, start, end):
	firstnum, secondnum, closep = square_parens(logic, 1)
	return Node(None, process_logic(logic[closep+1:]), None, 0, "F", "", firstnum, secondnum, logic[0:closep+1])

def andor_node(andor_info):
	return Node(None, process_logic(andor_info[0]), process_logic(andor_info[2]), 0, andor_info[1], "", None, None, andor_info[1])

#UNFINISHED - AP nodes need range from previous nodes (see notes)
def AP_node(AP_info,logic):
	return Node(None, None, None, 1, AP_info[1], AP_info[0], None, None, logic)
