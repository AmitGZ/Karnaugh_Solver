# Karnaugh Map Solver

This program receives the minterms and an unrestricted number of variables, and outputs the computed logical expression.

```python
>>> import karnaugh

>>> karnaugh.solve([3, 7, 11, 12, 15])
((A) && (B) && (!C) && (!D)) || ((C) && (D))
```
\
the program will use !,&&,|| as default logical operators, but this can be changed using the set_style method
```python
>>> karnaugh.set_style(not_symbol='not ', and_symbol=' and ', or_symbol=' or ', paranthesize_variables=False)
>>> karnaugh.solve([3, 7, 11, 12, 15])
(A and B and not C and not D) or (C and D)
```
\
the program will use capital alphabet for variables by default, but can also receive any input names, and more inputs than necessary.
```python
>>> karnaugh.solve([3, 7, 11, 12, 15], ['V', 'W', 'X', 'Y'])
((V) && (W) && (!X) && (!Y)) || ((X) && (Y))

>>> karnaugh.solve([3, 7, 11, 12, 15], ['V', 'W', 'X', 'Y', 'Z'])
((!V)) && (((W) && (X) && (!Y) && (!Z)) || ((Y) && (Z)))
```
