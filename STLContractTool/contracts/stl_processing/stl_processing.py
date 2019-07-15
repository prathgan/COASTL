import re
from gurobipy import *
from .stl_parsing import parse_logic
from .utilities.simple_utilities import remove_gurobi_log, parentheses_match

def process(logic, remove_log=False):
	"""
	Return result of passing logic expression into process_logic()
	"""
	if not parentheses_match(logic):
		raise ValueError("Opening and closing brackets do not match, check '(' and ')'")
	stl_tree = parse_logic(logic, None, None)
	# add constraints
	# solve problem
	if remove_log:
		remove_gurobi_log()
	return stl_tree

def synthesize_stl(m, ret_type=0):
	m.optimize()
	if ret_type==1:
		return m.getVars()
	else:
		return m
