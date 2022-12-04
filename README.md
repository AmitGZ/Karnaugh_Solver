# Karnaugh_Solver
Karnaugh map solver

This program receives the minterms, and an unrestricted number of variables and outputs the computed logical expression.\
the program will output capital alphabel by default but can also receive any input names.

```python
>>> karnaugh.solve([3, 7, 11, 12, 15], ['A', 'B', 'C', 'D', 'E', 'F'])
((A) && (B) && (!C) && (!D)) || ((C) && (D))
karnaugh.solve([3, 7, 11, 12, 15, 27], ['a', 'b', 'c', 'd', 'e'])
>>> ((!a) && (b) && (c) && (!d) && (!e)) || ((b) && (!c) && (d) && (e)) || ((!a) && (d) && (e))
```
