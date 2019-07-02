import re

def process(logic):
	"""
	Return result of passing logic expression into process_logic()
	"""
	if not parentheses_match(logic):
		raise ValueError("Opening and closing brackets do not match, check '(' and ')'")
	return process_logic(logic, 1)

def process_logic(logic, root):
	"""
	Return root of tree structure which represents
	a Signal Temporal Logic expression
	"""
	if logic=="":
		return []
	start,end = round_parens(logic, 0)
	andor_logic, andor_ind = find_andor(logic)
	if andor_logic != None and root==1:
		left_start, left_end, right_start, right_end = find_andor_children(logic,andor_ind)
		return Node(None, [process_logic(logic[1:left_end+1],1),process_logic(logic[right_start:len(logic)-1],1)], 0, andor_logic, "", None, None, andor_logic)
	elif andor_logic != None and root==0:
		left_start, left_end, right_start, right_end = find_andor_children(logic,andor_ind)
		return [Node(None, [process_logic(logic[1:left_end+1],1),process_logic(logic[right_start:len(logic)-1],1)], 0, andor_logic, "", None, None, andor_logic)]
	elif logic[0]=="~" and root==1:
		return Node(None, process_logic(logic[1:end+1],0), 0, "~", "", None, None, "~")
	elif logic[0]=="~" and root==0:
		return [Node(None, process_logic(logic[1:end+1],0), 0, "~", "", None, None, "~")]
	elif logic[start+1]=='G' or logic[start+1]=='F':
		firstnum, secondnum, closep = square_parens(logic,start+2)
		if root==1:
			return Node(None, process_logic(logic[closep+1:end], 0), 0, logic[start+1], "", firstnum, secondnum, logic[start+1:closep+1])
		else:
			return [Node(None, process_logic(logic[closep+1:end],0), 0, logic[start+1], "", firstnum, secondnum, logic[start+1:closep+1])]
	elif logic[start+1]=="~" and root==1:
		return Node(None, process_logic(logic[start+2:end],0), 0, "~", "", None, None, "~")
	elif logic[start+1]=="~" and root==0:
		return [Node(None, process_logic(logic[start+2:end],0), 0, "~", "", None, None, "~")]
	predicate_logic, predicate_ind = find_predicate(logic)
	var, minval, maxval = find_predicate_info(logic, predicate_ind, predicate_logic)
	if predicate_logic != None and root==1:
		return Node(None, [], 1, predicate_logic, var, minval, maxval, var+predicate_logic+str(minval if minval!=None else maxval))
	elif predicate_logic != None and root==0:
		return [Node(None, [], 1, predicate_logic, var, minval, maxval, var+predicate_logic+str(minval if minval!=None else maxval))]
	return []
