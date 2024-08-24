'''
Given an integer N, generate the Nth Catalan Number.


Input Format

First and only line of input contains a non-negative integer N.


Output Format

Print the Nth Catalan Number.


Constraints

0 <= N <= 10


Example

Input

3


Output

5


Explanation

3rd Catalan Number: 6C3 / 4 = 5
'''

def catlan(n):
  return factorial(2*n)//(factorial(n+1) * factorial(n))

def factorial(x):
  if x != 0:
    return x * factorial(x-1)
  else:
    return 1

n = int(input())
print(catlan(n))