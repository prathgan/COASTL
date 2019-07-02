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

def round_parens(string, start):
	"""
	Return indices of opening and closing parentheses
	of expression, starting from right side of expression
	"""
	count = 0
	itr_index = start
	first_not_found = 1
	end = None
	while itr_index<len(string):
		if string[itr_index]=='(':
			if first_not_found==1:
				start = itr_index
				first_not_found=0
			count = count + 1
		if string[itr_index]==')':
			count = count - 1
			if count==0:
				end = itr_index
				break
		itr_index += 1
	return start, end

def round_parens_bwd(string, start):
	"""
	Return indices of opening and closing parentheses
	of expression, starting from right side of expression
	"""
	count = 0
	itr_index = start
	first_not_found = 1
	end = None
	while itr_index>-1:
		if string[itr_index]==')':
			if first_not_found==1:
				end = itr_index
				first_not_found=0
			count = count + 1
		if string[itr_index]=='(':
			count = count - 1
			if count==0:
				start = itr_index
				break
		itr_index = itr_index - 1
	return start, end

def square_parens(string, start):
	"""
	Return the minimum and maximum of the range
	and index of closing bracket
	"""
	itr_index = start
	comma = 0
	closep = 0
	while itr_index<len(string):
		if string[itr_index]==',':
			comma = itr_index
		if string[itr_index]==']':
			closep = itr_index
			break
		itr_index += 1
	firstnum = float(string[start+1:comma])
	secondnum = float(string[comma+1:closep])
	return firstnum, secondnum, closep

def find_andor(string):
	"""
	Return logical operator and index which joins
	two halves of an expression
	"""
	operator = None
	paren_count = 0
	itr_index = 0
	operator_ind = -1
	while itr_index<len(string):
		if string[itr_index]=='(':
			paren_count = paren_count + 1
		if string[itr_index]==')':
			paren_count = paren_count - 1
		if paren_count==1 and (string[itr_index]=="&" or string[itr_index]=="|"):
			operator_ind = itr_index
			operator = string[itr_index:itr_index+1]
			return operator, operator_ind
		itr_index += 1
	return operator, operator_ind

def find_andor_children(string, andor_ind):
	"""
	Return indices of opening and closing brackets
	of expressions on either side of 'and' or 'or
	'"""
	right_start, right_end = round_parens(string,andor_ind+1)
	left_start, left_end = round_parens_bwd(string,andor_ind)
	return left_start, left_end, right_start, right_end

def find_predicate(string):
	"""
	Return logical operator of predicate expression
	and index of operator
	"""
	operator = None
	paren_count = 0
	itr_index = 0
	operator_ind = -1
	while itr_index<len(string):
		if string[itr_index]=='(':
			paren_count = paren_count + 1
		if string[itr_index]==')':
			paren_count = paren_count - 1
		if paren_count==1 and (string[itr_index]=="<" or string[itr_index]==">" or string[itr_index]=="="):
			operator_ind = itr_index
			if string[itr_index+1]=="=":
				operator = string[itr_index:itr_index+2]
			else:
				operator = string[itr_index]
			return operator, operator_ind
		itr_index += 1
	return operator, operator_ind

def find_predicate_info(string, operator_ind, operator):
	"""
	Return variable and its minimum and maximum values
	for a predicate expression
	"""
	var = find_predicate_var(string, operator_ind)
	minval = None
	maxval = None
	if operator=="<=" or operator=="<":
		maxval = find_predicate_num(string, operator_ind+len(operator)-1)
	elif operator==">=" or operator==">":
		minval = find_predicate_num(string, operator_ind+len(operator)-1)
	elif operator=="=":
		maxval = find_predicate_num(string, operator_ind+len(operator)-1)
		minval = maxval
	return var, minval, maxval

def find_predicate_num(string, last_operator_ind):
	"""
	Return number from predicate expression string
	"""
	itr_index = last_operator_ind
	while itr_index<len(string):
		if string[itr_index]==")":
			return float(string[last_operator_ind+1:itr_index])
		itr_index += 1
	return -1

def find_predicate_var(string, operator_ind):
	"""
	Return variable from predicate expression string
	"""
	itr_index = operator_ind
	while itr_index>-1:
		if string[itr_index]=="(":
			return string[itr_index+1:operator_ind]
		itr_index = itr_index - 1
	return -1

def parentheses_match(string):
	"""
	Return True if opening and closing brackets are
	all matched in an input logical expression
	"""
	verification_stack = []
	matched = True
	itr_index = 0
	while itr_index < len(string) and matched:
		if string[itr_index]=="(":
			verification_stack.append(string[itr_index])
		elif string[itr_index]==")":
			if len(verification_stack)==0:
				matched = False
			else:
				verification_stack.pop()
		itr_index += 1
	return matched and len(verification_stack) == 0
