import re
from gurobipy import *
from .stl_parsing import parse_logic
from .stl_constraints import create_constraints
from .utilities.simple_utilities import remove_gurobi_log, parentheses_match

def parse_stl(logic, remove_log=False):
	"""Parses string of STL logic into an STL tree"""
	if not parentheses_match(logic):
		raise ValueError("Opening and closing brackets do not match, check '(' and ')'")
	stl_tree = parse_logic(logic, None, None)
	return stl_tree

def synthesize_stl(stl_node, ret_type=0, remove_log=False, console_log=True, maximize_vars=None, minimize_vars=None):
	"""creates constraints and synthesizes solutions for variables in STL tree, returns optimized model"""
	m = create_constraints(stl_node, maximize_vars=maximize_vars, minimize_vars=minimize_vars, console_log=console_log)
	m.optimize()
	if remove_log:
		remove_gurobi_log()
	if ret_type==1:
		return m.getVars()
	else:
		return m

def create_model_stl(stl_node, remove_log=False, console_log=True, maximize_vars=None, minimize_vars=None):
	"""Creates constrained MILP gurobi model for STL tree"""
	return create_constraints(stl_node, maximize_vars=maximize_vars, minimize_vars=minimize_vars, console_log=console_log)

def synthesize_stl(m, ret_type=0):
	"""Synthesizes solutions for variables in model m by optimizing model"""
	m.optimize()
	if ret_type==1:
		return m.getVars()
	else:
		return m
