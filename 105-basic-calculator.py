'''
Given a mathematical expression consisting of integers, addition, subtraction, multiplication, division, and modulo operators. Evaluate the expression and print the result.

Note:
Assume that it is a regular Calculator, where the expression will be simply evaluated from left to right, without following BODMAS Rule.
Assume that the division operator will give an integer value.
Assume that the modulo operator (say % M) will give a positive integer value in the range [0, M-1]
Examples:

3 - 8 / 2 = -5 / 2 = -2
3 + 8 / 2 = 11 / 2 = 5
2 - 9 % 5 = -7 % 5 = 3
Input Format

The first line of input contains an integer N. The second line of input is a single line containing a mathematical expression. The expression will contain N integers, and (N-1) operators, separated by single spaces.


Output Format

Print a single integer, representing the result of the evaluated expression.


Constraints

2 <= N <= 8

1 <= Integer in the Expression <= 9


Example

Input

6
8 + 2 * 5 - 3 / 5 % 6


Output

3


Explanation

8 + 2 * 5 - 3 / 5 % 6

= 10 * 5 - 3 / 5 % 6

= 50 - 3 / 5 % 6

= 47 / 5 % 6

= 9 % 6

= 3
'''

n = int(input())
exp = input()
comp = exp.split()
result = int(comp[0])
for i in range(1, len(comp), 2):
    op = comp[i]
    nxt = int(comp[i+1])

    if op == '+':
        result += nxt
    elif op == '-':
        result -= nxt
    elif op == '*':
        result *= nxt
    elif op == '/':
        result = int(result/ nxt)
    elif op == '%':
        result %= nxt
print(result)