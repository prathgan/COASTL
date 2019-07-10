from gurobipy import *

def create_constraints(tree, m=None):
    if m == None:
        m = Model("solver")
    m = create_constraints()
