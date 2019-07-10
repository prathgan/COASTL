from gurobipy import *
from .utilities.simple_utilities import get_bin_name
from .stl_parsing_helpers import SwitchDict

def create_constraints(tree, m=None):
    if m == None:
        m = Model("solver")
    m = topmost_constr(node, m)
    node_switch = SwitchDict([("~",not_constr),
                              ("G",g_constr),
                              ("F",f_constr),
                              ("<=",leq_constr),
                              (">=",geq_constr),
                              ("<",l_constr)])
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

def g_constr(node, m):
    def g(start_t, end_t):
        times = list(range(start_t, end_t))
        for t in times:
            # exec()
