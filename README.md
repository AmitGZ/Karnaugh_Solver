# Karnaugh Map Solver

This program receives the minterms and an unrestricted number of variables, and outputs the computed logical expression.\

```python
>>> import karnaugh

>>> karnaugh.solve([3, 7, 11, 12, 15])
(A && B && !C && !D) || (C && D)
```
\
the program will output !,&&,|| as default logical operators but this can be changed using the set_style method
```python
>>> karnaugh.set_style(not_symbol='Not ', and_symbol=' And ', or_symbol=' Or ', paranthesize_variables=False)
>>> karnaugh.solve([3, 7, 11, 12, 15])
(A And B And Not C And Not D) Or (C And D)
```
\
the program will output capital alphabet by default but can also receive any input names.
```python
>>> karnaugh.solve([3, 7, 11, 12, 15], ['V', 'W', 'X', 'Y', 'Z'])
((V) && (W) && (!X) && (!Y)) || ((X) && (Y))
```
