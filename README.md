# COASTL (Contract Operations and Signal Temporal Logic)
[Poster](https://www.github.com/prathgan/coastl/media/poster.pdf)

Lightweight Python package for doing operations concerning A/G contracts in design-by-contract systems design. Also has functionality to read Signal Temporal Logic into operable structure and derive corresponding boolean and synthesis constraints. Developed at DesCyPhy Lab, USC.

## Installation
### Prerequisites
For the following prerequisites, if not already installed, a `pip install` should suffice:
- `sympy`
- `numpy`
- `re`

This package also requires a functioning installation of Gurobi, an optimization solver tool used heavily in coastl. Once you have installed [Gurobi](https://www.gurobi.com), navigate to the Gurobi `<intstalldir>` and execute `python setup.py install`.
### Install coastl
1) download .zip file of this repository

2) navigate to directory where coastl `setup.py` file is located

3) `pip install .`
## Use
For more, see [the examples folder](https://github.com/prathgan/coastl/examples).
### Signal Temporal Logic
Import functions:
```python
from coastl import parse_stl, create_model_stl, synthesize_stl
```
Create tree from STL:
```python
stl_tree = parse_stl("G[0,10]((x<=10)&&(~(x<=5)))")
```
Traverse tree and create model, adding constraints for all logic:
```python
m = create_model_stl(stl_tree)
```
Optimize model and synthesize values for x:
```python
m = synthesize_stl(m)
```
Get list of variables (type is Gurobi variables):
```python
solved_vars = m.getVars()
```
Print variable names and values:
```python
for var in solved_vars:
  print(var.VarName + ": " + str(var.X))
```
### Contracts
Import Contract object, conjunction & composition operations
```python
from coastl import Contract, conjunction
```
Create two contracts in the format [vars, assumptions, guarantees]
```python
c1 = Contract(["x"],"T","(x<=2)")
c2 = Contract(["x"],"T","~(x<=1)")
```
Saturate both contracts
```python
c1.saturate()
c2.saturate()
```
If contracts in an operation are not already saturated, coastl will automatically saturate them.

Composition:
```python
c3 = composition([c1, c2])
c3.synthesize(remove_log=True, console_log=False)
c3_solutions = c3.get_synthesized_vars()
print(c3_solutions)
```

Conjunction:
```python
c3 = conjunction([c1, c2])
c3.synthesize(remove_log=True, console_log=False)
c3_solutions = c3.get_synthesized_vars()
print(c3_solutions)
```
## Contact
This library is currently not in active development. If you have any questions about the operation of this package or would like to contribute, please email me directly at gandhips02@gmail.com. Additionally, I'm still working on documenting all the code, and a big update is coming soon with docstring documentations of each method and class in the package. If you'd like to help me with this, please send me an email.
