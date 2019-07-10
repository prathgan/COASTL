# not
b_inner == 1 - b_not

# and
2 * b_and <= b_inner_1 + b_inner_2
b_inner_1 + b_inner_2 <= 1 + b_and

# or
b_or <= b_inner_1 + b_inner_2
b_inner_1 + b_inner_2 <= 2 * b_or

# implies
b_left + b_right >= b_implies
2 * b_implies >= 1 - b_left + b_right

# globally
def g(start_t, end_t):
    times = list(range(start_t, end_t))
    for t in times:
        # exec()


if not m.getVars()[-1].varName==self_temp_bin_name:
    exec(self_temp_bin_name+"=m.addVar(vtype=GRB.BINARY, name='"+self_temp_bin_name+"')")
