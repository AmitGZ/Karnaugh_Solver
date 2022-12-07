# Karnaugh Map Solver

This program receives the minterms and an unrestricted number of variables, and outputs the computed logical expression.\
the program will output capital alphabel by default but can also receive any input names.

```python
>> > import karnaugh

>> > Karnaugh.solve([3, 7, 11, 12, 15])
(A & & B & & !C & & !D) | | (C & & D)

>> > Karnaugh.solve([3, 7, 11, 12, 15], ['A', 'B', 'C', 'D', 'E'])
(!A) & & ((B & & C & & !D & & !E) | | (D & & E))

>> > Karnaugh.solve([3, 7, 11, 12, 15, 27], ['V', 'W', 'X', 'Y', 'Z'])
(!V & & W & & X & & !Y & & !Z) | | (W & & !X & & Y & & Z) | | (!V & & Y & & Z)

```
