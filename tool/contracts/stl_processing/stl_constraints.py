from gurobipy import *
from .utilities.simple_utilities import get_bin_name
from .stl_parsing_helpers import SwitchDict

def create_constraints(node, m=None):
    if m == None:
        m = Model("solver")
    m = topmost_constr(node, m)
    node_switch = SwitchDict([("~",not_constr),
                              ("&&", and_constr),
                              ("G",g_constr),
                              ("F",f_constr),
                              ("<=",leq_constr),
                              (">=",geq_constr)])
    m = node_switch[node.logic](node, m)
    if node.child1 is not None:
        m = create_constraints(node.child1, m)
    if node.child2 is not None:
        m = create_constraints(node.child2, m)
    return m

def topmost_constr(node, m):
    if node.parent is None:
        bin_name = get_bin_name(node)
        exec(bin_name+"= m.addVar(vtype=GRB.BINARY, name='b_"+node.string_rep+"')")
        exec("m.addConstr("+bin_name+" == 1, 'c_"+bin_name+"')")
    return m

def not_constr():
    pass

def and_constr(node, m):
    pass

def g_constr(node, m):
    bin_name = get_bin_name(node)
    child_bin_name = get_bin_name(node.child1)
    exec(bin_name+"=m.addVar(vtype=GRB.BINARY, name='"+bin_name+"')")
    times = list(range(node.range_start, node.range_end))
    sum_bin_allTs = ""
    n = 0
    for t in times:
        temp_bin = child_bin_name+"_"+str(t)
        exec(temp_bin+"=m.addVar(vtype=GRB.BINARY, name='"+temp_bin+"')")
        sum_bin_allTs += temp_bin + "+"
        n += 1
    sum_bin_allTs = sum_bin_allTs[:-1]
    exec("m.addConstr("+ str(n) + "*" + bin_name + " <= " + sum_bin_allTs + ", 'c_" + bin_name + "_1')")
    exec("m.addConstr("+ sum_bin_allTs + " <= " + str(n-1) + " + " + bin_name + ", 'c_"+bin_name+"_1')")

def f_constr():
    pass

def leq_constr():
    pass

def geq_constr(node, m):
    print(node)
    pass
