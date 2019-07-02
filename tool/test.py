# from stl_processing.stl_helper_funcs import *
# from stl_processing.stl_processing import *
# from stl import Node
# from contract import Contract
# from operations import *
# from utilities import *
# from timeit import default_timer as timer
# from sympy.logic import simplify_logic
# from sympy.abc import *
# from sympy import S
from contracts.contract import *

"""
timing toolkit:
start = timer()
end = timer()
print(end - start)
"""


c1 = Contract(["x","y"],"(x(1)<=10)&((y<=20))","~(~(G[0,10](F[1,3](~(x>=1)&(y<=0)))))")
c1.saturate()

# start, end = round_parens("x<=10")
# print(predicate("x<=10", start, end))
# print(process("(~(F[1,10]((x>=1)&(y<=0))))&(~(F[1,10]((x>=1)&(y<=0))))"))


# start = timer()
# root = (process("((!(G[0,10](F[1,3](!(x>=1)&&(xy<=0)))))&&(!(G[0,10](F[1,3](!(x>=1)&&(xy<=0))))))"))
# end = timer()
# print(end - start)
