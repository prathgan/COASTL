# import library, import Contract class
from STLContractTool import Contract

# create Contract objects with format C([Variables],Assumptions,Guarantees)
c1 = Contract(["x"],"T","G[0,10](x<=1)")
c2 = Contract(["y","z"],"(y<=10)&&((z<=20))","G[0,10]((y<=1)&&(z<=0))")
c3 = Contract(["p","q"],"T","G[0,10]((p+q)<=2)")

# synthesize values for variables
# note: contracts must be resynthesized after being edited
c1.synthesize(remove_log=True)
c2.synthesize(remove_log=True)
c3.synthesize(remove_log=True)

# get synthesized values for variables considered in contract
c1_solutions = c1.get_synthesized_vars()
c2_solutions = c2.get_synthesized_vars()
c3_solutions = c3.get_synthesized_vars()

# print solutions for variables
print(c1_solutions)
print(c2_solutions)
print(c3_solutions)
