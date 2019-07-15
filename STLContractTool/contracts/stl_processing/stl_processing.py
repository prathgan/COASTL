import re
from gurobipy import *
from .stl_parsing import parse_logic
from .stl_constraints import create_constraints
from .utilities.simple_utilities import remove_gurobi_log, parentheses_match

def parse_stl(logic, remove_log=False):
	"""

	"""
	if not parentheses_match(logic):
		raise ValueError("Opening and closing brackets do not match, check '(' and ')'")
	stl_tree = parse_logic(logic, None, None)
	return stl_tree

def synthesize_stl(stl_node, ret_type=0, remove_log=False):
	m = create_constraints(stl_node)
	m.optimize()
	if remove_log:
		remove_gurobi_log()
	if ret_type==1:
		return m.getVars()
	else:
		return m
