from contract import Contract

def conjunction(contracts):
	if len(contracts)>2:
		return two_contract_conjunction(contracts[0],conjunction(contracts[1:]))
	else:
		return two_contract_conjunction(contracts[0],contracts[1])

def two_contract_conjunction(c1,c2):
	return Contract(list_union(c1.variables,c2.variables),
		Node(None, [c1.assumptions,c2.assumptions], 0, "||", list_union(c1.assumptions.vars,c2.assumptions.vars), None, None, "||"),
		Node(None, [c1.guarantees,c2.guarantees], 0, "||", list_union(c1.guarantees.vars,c2.guarantees.vars), None, None, "||"))
