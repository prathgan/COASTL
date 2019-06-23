from contract import Contract

def conjunction(contracts):
	if len(contracts)>2:
		return two_contract_conjunction(contracts[0],conjunction(contracts[1:]))
	else:
		return two_contract_conjunction(contracts[0],contracts[1])

def two_contract_conjunction(c1,c2):
	return Contract(list_union(c1.variables,c2.variables),
		list_union(c1.assumptions,c2.assumptions),
		list_union(c1.guarantees,c2.guarantees))

def list_union(l1,l2):
	return list(set().union(l1,l2))