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
	firstnum = int(string[start+1:comma])
	secondnum = int(string[comma+1:closep])
	return firstnum, secondnum, closep

def connector(string):
	"""
	Return logical operator and index which joins
	two halves of an expression
	"""
	operator = None
	paren_count = 0
	itr_index = 0
	while itr_index<len(string):
		if string[itr_index]=='(':
			paren_count = paren_count + 1
		if string[itr_index]==')':
			paren_count = paren_count - 1
		if paren_count==0 and (string[itr_index]=="&" or string[itr_index]=="|" or string[itr_index]=="-"):
			return string[:itr_index], string[itr_index:itr_index+2], string[itr_index+2:]
		if paren_count==0 and string[itr_index]=="U":
			return string[:itr_index], string[itr_index:itr_index+1], string[itr_index+1:]
		itr_index += 1
	return -1

def predicate(logic, start, end):
	"""Returns information about predicate logic from string form if is predicate"""
	is_p, equals_ind = is_predicate(logic, start, end)
	if is_p:
		return predicate_info(logic, start, equals_ind)
	else:
		return -1

def is_predicate(logic, start, end):
	"""Returns T/F depending on if logic string is predicate and index of predicate operator (<=)"""
	equals_ind = logic.index("=")
	if equals_ind>end or equals_ind<start:
		return True, equals_ind
	return False, -1

def predicate_info(logic, start, equals_ind):
	"""Returns information about predicate logic from string form"""
	var = logic[0:equals_ind]
	operator = "="
	if var[-1]=="<" or var[-1]==">":
		operator = var[-1] + operator
		var = var[:-1]
	return var, operator

def remove_operators(str):
	"""Returns logic string with operators removed"""
	str = str.replace('+','')
	str = str.replace('-','')
	str = str.replace('*','')
	str = str.replace('/','')
	str = str.replace('(','')
	str = str.replace(')','')
	return str

class SwitchDict(dict):
	"""Dictionary subclass with dict.get(x), where x is not in dict, returning None"""
    def __getitem__(self, key):
        return dict.get(self, key)
