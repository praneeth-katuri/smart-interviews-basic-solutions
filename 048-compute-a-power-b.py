'''
Given two integers A and B, compute A power B.


Note: Do not use any inbuilt functions / libraries for your main logic.

Input Format

The first and only line of input contains two positive integers A and B.


Output Format

Print A power B.


Constraints

1 <= A <= 100

0 <= B <= 9


Example

Input

2 3


Output

8


Explanation

Self Explanatory
'''

a, b = map(int, input().split())
print(a**b)