from gurobipy import *

m = Model("F[0,1]((x(2)>=0)&&(x(2)<=0))")

# F[0,1] node
b0 = m.addVar(vtype=GRB.BINARY, name="b0")
m.addConstr(b0 == 1, "c0")

# && node
b1_0 = m.addVar(vtype=GRB.BINARY, name="b1_0")
b1_1 = m.addVar(vtype=GRB.BINARY, name="b1_1")
m.addConstr(b0 <= b1_0 + b1_1, "c1")
m.addConstr(b1_0 + b1_1 <= 2 * b0, "c2")

# x(2)>=0 node create vars
b2_0 = m.addVar(vtype=GRB.BINARY, name="b2_0")
b2_1 = m.addVar(vtype=GRB.BINARY, name="b2_1")

# x(2)<=0 node create vars
b3_0 = m.addVar(vtype=GRB.BINARY, name="b3_0")
b3_1 = m.addVar(vtype=GRB.BINARY, name="b3_1")

# (x(2)>=0) && (x(2)<=0)
m.addConstr(2 * b1_0 <= b2_0 + b3_0, "c3")
m.addConstr(b2_0 + b3_0 <= 1 + b1_0, "c4")
m.addConstr(2 * b1_1 <= b2_1 + b3_1, "c5")
m.addConstr(b2_1 + b3_1 <= 1 + b1_1, "c6")

m.optimize()

for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
