'''
For a given positive integer - N, compute Nth Fibonacci number.


Input Format

The first and only line of input contains a positive number - N.


Output Format

Print the Nth fibonacci number.


Constraints

0 <= N <= 20


Example

Input

4


Output

3

Explanation

The fibonacci series:

0, 1, 1, 2, 3, 5, 8,......

At 4th position, we have 3.
'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))