from gurobipy import *

def create_constraints(tree, m=None):
    if m == None:
        m = Model("solver")
    m = topmost_constr(node, m)
    node_switch = SwitchDict([("~",not_constr),
                              ("G",g_constr),
                              ("F",f_constr),
                              ("<=",leq_constr),
                              (">=",geq_constr)])
    m = node_switch[tree.logic](node, m)
    if tree.child1 is not None:
        m = create_constraints(tree.child1, m)
    if tree.child2 is not None:
        m = create_constraints(tree.child2, m)
    return m

def topmost_constr(node, m):
    if node.parent is None:
        bin_name = "b_"+node.string_rep
        exec(bin_name+"= m.addVar(vtype=GRB.BINARY, name='b_"+node.string_rep+"')")
        exec("m.addConstr("+bin_name+" == 1, 'c_"+bin_name+"')")
    return m

def g_constr(node, m):
    def g(start_t, end_t):
        times = list(range(start_t, end_t))
        for t in times:
            # exec()
