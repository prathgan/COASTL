from gurobipy import *

def create_constraints(tree, m=None):
    if m == None:
        m = Model("solver")
    
    if tree.child1 is not None:
        m = create_constraints(tree.child1, m)
    if tree.child2 is not None:
        m = create_constraints(tree.child2, m)
    return m
