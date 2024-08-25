'''
There are six positive integers A, B, C, D, E, and F, which satisfy A × B × C ≥ D × E × F. Find the remainder when (A × B × C) - (D × E × F) is divided by (1e9+7).

Note:

1. (X × Y) % M = (X % M × Y % M) % M

2. (X - Y) % M = (X % M - Y % M + M) % M


Input Format

The first and only line of input contains six space-separated integers A, B, C, D, E, and F.


Output Format

For the given input, print a single line representing the answer.


Constraints

0 ≤ A, B, C, D, E, F ≤ 1018

A × B × C ≥ D × E × F


Example

Input

2 3 5 1 2 4


Output

22


Explanation

Since A × B × C = 2 × 3 × 5 = 30 and D × E × F = 1 × 2 × 4 = 8, we have (A × B × C) - (D × E × F) = 22. When you divide 22 by (1e9+7), the remainder will be 22.
'''

a,b,c,d,e,f = map(int, input().split())
print(((a*b*c)-(d*e*f))%1000000007)