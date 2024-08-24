'''
Given a non-negative number - N. Print N!


Input Format

The first and only line of input contains a number - N.


Output Format

Print factorial of N.


Constraints

0 <= N <= 10


Example

Input

5


Output

120


Explanation

Self Explanatory
'''


n = int(input())

def factorial(n):
    if n != 0:
        fact = n * factorial(n-1)
        return fact
    elif n == 0:
        return 1

print(factorial(n))