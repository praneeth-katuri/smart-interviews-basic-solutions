'''
Write a program to calculate the amount of money accrued from compound interest.

Compound interest is the interest calculated on the initial principal and also on the accumulated interest of previous periods. Given the principal amount (P), the annual interest rate (R), the number of times the interest is compounded per year (N), and the time in years (T), write a program to calculate the final amount (A) after the specified time.

Compound Interest = P(1 + R/N)NT - P

Always consider the floor value of (R/N) while computing Compound Interest.


Input Format

The first and only line of input contains 4 integers P, R, N, T separated by spaces.


Output Format

Print the Compound Interest for the given values of P, R, N, T.


Constraints

1 <= P <= 100

1 <= R <= 10

1 <= N, T <= 5


Example

Input

65 6 1 2


Output

3120


Explanation

Self Explanatory
'''

import math
p, r, n, t = map(int, input().split())
rate = math.floor(r/n)
a = p * ( 1+rate) ** (n*t)
ci = a - p
print(int(ci))