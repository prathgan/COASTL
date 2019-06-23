from contract import Contract
from stl import Node
from operations import *
from utilities import *
from stl import *

# Contract(Variables, Assumptions, Guarantees)
c1 = Contract(["x","y"], ["x>=10","y<6"], ["return x+1","return y-1"])
c2 = Contract(["y","z"], ["y<6","z>20"], ["return y+1","return z-1"])
c3 = Contract(["t","s"], ["s<15","t>12"], ["return t+3","return z-1"])

#conjoined = (conjunction([c1,c2,c3]))
#display(conjoined)

process_logic("!G[0,10](F[1,3](!(x>=1)&&(y<=0))")