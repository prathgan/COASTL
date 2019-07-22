from coastl import parse_stl, create_model_stl, synthesize_stl

stl_tree = parse_stl("G[0,10]((x<=10)&&(~(x<=5)))")
m = create_model_stl(stl_tree)
m = synthesize_stl(m)
solved_vars = m.getVars()
print(solved_vars)
