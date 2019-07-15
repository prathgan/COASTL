# from stl_processing.stl_helper_funcs import *
# from stl_processing.stl_processing import *
# from stl import Node
# from contract import Contract
# from operations import *
# from utilities import *
from timeit import default_timer as timer
# from sympy.logic import simplify_logic
# from sympy.abc import *
# from sympy import S
from contracts.contract import *
from contracts.operations import *
from contracts.stl_processing.stl_constraints import *
from contracts.stl_processing.stl_constraints_helpers import *
from contracts.stl_processing.utilities.object_utilities import *
import sympy
from gurobipy import *


"""
timing toolkit:
start = timer()
end = timer()
print(end - start)
"""

#tree = process("F[0,10]((~(x<=1))&&(x<=10))")
# tree = process("~(x<=2)")
#m = create_constraints(tree, remove_log=True)
# print(m.getConstrs())
#m.optimize()
#display_model(m)

c = Contract(["x","y"],"T","G[0,10]((~(x<=1))&&(y<=10))")
print(c.synthesize())

# print(isolate_0(process("(x<=1)")))

#tree = process("(F[0,20]((5<=x(1))&&(x(1)<=5)&&(0<=x(2))&&(x(2)<=0)))U(F[0,20]((5<=x(1))&&(x(1)<=5)&&(0<=x(2))&&(x(2)<=0)))")
#print(tree.vars)
# remove_gurobi_log()
# print(tree.child1.child1.child2.child2.child1)
# print(tree.child1.child1.child2.child2.child1.parent)

# c1 = Contract(["x","y"],"(x(1)<=10)&&((y<=20))","~(~(G[0,10](~(x>=1)&&(y<=0))))")
# c2 = Contract(["x","y"],"(x(1)<=10)&&((y<=20))","F[1,3]((~(x>=1))&&(y<=0))")
# conjunction(c1,c2)
#print(end - start)
# composition(c1,c2)
#print(end - start)

# start, end = round_parens("x<=10")
# print(predicate("x<=10", start, end))
# print(process("(~(F[1,10]((x>=1)&(y<=0))))&(~(F[1,10]((x>=1)&(y<=0))))"))


# start = timer()
# root = (process("((!(G[0,10](F[1,3](!(x>=1)&&(xy<=0)))))&&(!(G[0,10](F[1,3](!(x>=1)&&(xy<=0))))))"))
# end = timer()
# print(end - start)
