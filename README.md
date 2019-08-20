## Unit Testing Assignment

by Sirikon Songsaengthong.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| many items,many times, many orders  |  list with one of duplicate items, items in same order  |


## Test Cases for Fraction

Test cases for __str__ 

| Test case                         |  Expected Result         |
|-----------------------------------|--------------------------|
| Numerator > 0 , Denominator = 0   |   1/0                    |
| Numerator < 0 , Denominator = 0   |  -1/0                    |
| Denominator != 0                  |  Numerator/Denominator   |
| Numerator < 0 or Denominator < 0  |  -Numerator/Denominator  |
| Only Numerator or Denominator = 1 |  Numerator               |

Test cases for __add__ 

| Test case                         |  Expected Result         |
|-----------------------------------|--------------------------|
| Positive fractions add together   |   Positive fraction      |
| Negative fractions add together   |   Negative fraction      |

Test cases for __sub__ 

| Test case                             |  Expected Result             |
|---------------------------------------|------------------------------|
| Positive fractions substract together |  Positive/Negative fraction  |
| Negative fractions substract together |  Positive/Negative fraction  |
| Any fractions substract with 0        |  The same fraction           |

Test cases for __mul__ 

| Test case                                         |  Expected Result     |
|---------------------------------------------------|----------------------|
| Positive fractions multiple together              |  Positive fraction   |
| Negative fractions multiple together              |  Positive fraction   |
| Positive and Negative fractions multiple together |  Negative fraction   |

Test cases for __eq__ 

| Test case                                   |  Expected Result |
|---------------------------------------------|------------------|
| Proper form so the internal representation  |  Equal           |
| Proper form and other fraction              |  Equal           |

Test cases for __gt__ 

| Test case                      |  Expected Result  |
|--------------------------------|-------------------|
| Fraction greater than another  |  True             |
| Fraction smaller than another  |  False            |
| Both are equal                 |  False            |

Test cases for __neg__ 

| Test case            |  Expected Result      |
|----------------------|-----------------------|
| Positive fraction    |   Negative fraction   |
| Negative fraction    |   Positive fraction   |

















