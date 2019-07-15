from .contract import Contract
from .stl_processing.utilities.simple_utilities import *
from .stl_processing.stl_node import Node
import copy

def conjunction(c1,c2=None):
	if c2 is not None:
		return two_contract_conjunction(c1,c2)
	else:
		if len(c1)>2:
			return two_contract_conjunction(c1[0],conjunction(c1[1:]))
		else:
			return two_contract_conjunction(c1[0],c1[1])

def two_contract_conjunction(c1,c2):
	if c1.isSat == 0:
		c1.saturate()
	if c2.isSat == 1:
		c2.saturate()
	return Contract(list_union(c1.variables,c2.variables),
		Node(None, c1.assumptions, c2.assumptions, 0, "||", list_union(c1.assumptions.vars,c2.assumptions.vars), None, None, "||"),
		Node(None, c1.guarantees, c2.guarantees, 0, "&&", list_union(c1.guarantees.vars,c2.guarantees.vars), None, None, "&&"))

def composition(c1, c2=None):
	if c2 is not None:
		return two_contract_composition(c1,c2)
	else:
		if len(c1)>2:
			return two_contract_composition(c1[0],composition(c1[1:]))
		else:
			return two_contract_composition(c1[0],c1[1])

def two_contract_composition(c1,c2):
	if c1.isSat == 0:
		c1.saturate()
	if c2.isSat == 1:
		c2.saturate()
	guarantee_new = Node(None, c1.guarantees, c2.guarantees, 0, "&&", list_union(c1.guarantees.vars,c2.guarantees.vars), None, None, "&&")
	not_guarantee = Node(None, copy.deepcopy(guarantee_new), None, 0, "~", guarantee_new.vars, None, None, "~")
	assumption_new_inter = Node(None, c1.assumptions, c2.assumptions, 0, "&&", list_union(c1.assumptions.vars,c2.assumptions.vars), None, None, "&&")
	assumption_new = Node(None, assumption_new_inter, not_guarantee, 0, "||", list_union(assumption_new_inter.vars,not_guarantee.vars), None, None, "||")
	return Contract(list_union(c1.variables,c2.variables),assumption_new,guarantee_new)
