from contract import Contract
from stl import Node
from operations import *
from utilities import *
from stl import *

# Contract(Variables, Assumptions, Guarantees)
#c1 = Contract(["x","y"], ["(x>=10)","(y<6)"], ["(x=1)","(y<1)"])
#print(c1.guarantees)
# c2 = Contract(["y","z"], ["y<6","z>20"], ["return y+1","return z-1"])
# c3 = Contract(["t","s"], ["s<15","t>12"], ["return t+3","return z-1"])

#conjoined = (conjunction([c1,c2,c3]))
#display_contract(conjoined)

#root = process_logic("!G[0,10](F[1,3](!(x>=1)&&(y<0))")
#print(root)
print(process("(x=10)"))

# print(process("!(G[0,1234](F[1234,1234](!((x>=1234)&&(y<=1234)))))"))
# print(process("(G[0,10])"))
# print(square_parens("(G[0,10])",2))
# print(process_logic("(x<=10)",1))
# print(find_andor("(!(x>=1)||(y<=0))"))
# andor_logic, andor_ind = (find_andor("(!(x>=1)||(y<=0))"))
# print(find_andor_children("(!(x>=1)||(y<=0))",andor_ind))

# root = Node(None, [], 0, "!", ["x"], None, None)
# child_layer_1 = Node(root, [], 0, "G", ["x"], 0, 10)
# child_layer_2 = Node(child_layer_1, [], 1, ">=", ["x"], None, 10)
# root.children = [child_layer_1]
# child_layer_1.children = [child_layer_2]

# print(root)
