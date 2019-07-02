def round_parens(string, start=0):
	"""
	Return indices of opening and closing parentheses
	of expression, starting from right side of expression
	"""
	count = 0
	itr_index = start
	first_not_found = 1
	end = 0
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

def predicate(logic, start, end):
	is_p, equals_ind = is_predicate(logic, start, end)
	if is_p:
		return predicate_info(logic, start, equals_ind)
	else:
		return -1

def is_predicate(logic, start, end):
	equals_ind = logic.index("=")
	if equals_ind>end or equals_ind<start:
		return True, equals_ind
	return False, -1

def predicate_info(logic, start, equals_ind):
	num = float(logic[equals_ind+1:-1]+logic[-1])
	var = logic[0:equals_ind]
	operator = "="
	if var[-1]=="<" or var[-1]==">":
		operator = var[-1] + operator
		var = var[:-1]
	return var, operator, num
