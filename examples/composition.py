# import library, import Contract class
from STLContractTool import Contract
from STLContractTool import composition

# create Contract objects with format C([Variables],Assumptions,Guarantees)
# note: if no range is provided in STL (no G[] or F[]), assumes range 0-0
c1 = Contract(["x"],"T","(x<=2)")
c2 = Contract(["x"],"T","~(x<=1)")
c3 = Contract(["y"],"T","(y<=3)")
c4 = Contract(["x","y"],"T","x+y<=5")

# perform conjunction of Contracts c1, c2, and c3
c5 = composition([c1, c2, c3, c4])

# synthesize values for variables
# note: contracts must be resynthesized after being edited
# note: remove_log and console_log parameters set to False
#       so gurobi log file removed and logging put to console
c5.synthesize(remove_log=True, console_log=False)

# get synthesized values for variables considered in contract
c5_solutions = c5.get_synthesized_vars()

# print solutions for variables
print(c5_solutions)

#-----------------------------#

# create Contract objects with format C([Variables],Assumptions,Guarantees)
# note: if no range is provided in STL (no G[] or F[]), assumes range 0-0
c6 = Contract(["y"],"T","(y<=2)")
c7 = Contract(["y"],"T","~(y<=1)")

# perform conjunction of Contracts c6 and c7
# note: this is different from the first example becuase it has only two contracts
c8 = composition(c6, c7)

# synthesize values for variables
# note: contracts must be resynthesized after being edited
# note: remove_log and console_log parameters set to False
#       so gurobi log file removed and logging put to console
c8.synthesize(remove_log=True, console_log=False)

# get synthesized values for variables considered in contract
c8_solutions = c8.get_synthesized_vars()

# print solutions for variables
print(c8_solutions)
