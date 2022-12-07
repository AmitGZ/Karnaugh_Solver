# Karnaugh Map Solver

This program receives the minterms and an unrestricted number of variables, and outputs the computed logical expression.\
the program will output capital alphabel by default but can also receive any input names.

```python
>>> import karnaugh

>>> karnaugh.solve([3, 7, 11, 12, 15])
(A && B && !C && !D) || (C && D)
```

the program will output capital alphabel by default but can also receive any input names.
```python
>>> karnaugh.set_style(not_symbol='not ', and_symbol=' and ', or_symbol=' or ', paranthesize_variables=False)
>>> karnaugh.solve([3, 7, 11, 12, 15, 27], ['V', 'W', 'X', 'Y', 'Z'])
(Not V And W And X And Not Y And Not Z) Or (W And Not X And Y And Z) Or (Not V And Y And Z)


```
