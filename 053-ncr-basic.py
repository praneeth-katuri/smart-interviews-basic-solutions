'''
Given two numbers N and R, find the value of NCR.


Input Format

The first and only line of input contains integers N and R.


Output Format

Print the value of NCR


Constraints

1 <= N <= 10

1 <= R <= 10


Example

Input

5 3


Output

10


Explanation

Self Explanatory
'''

n, r = map(int, input().split())
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

if n < r: 
    print(0)
else:
    print(factorial(n)//(factorial(n-r) * factorial(r)))