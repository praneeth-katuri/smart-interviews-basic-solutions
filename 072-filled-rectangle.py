'''
Given N and M, print the following rectangle pattern of size N × M. See examples for more details.


Input Format

The first line of input contains N and M.


Output Format

Print the rectangle pattern.


Constraints

1 <= N <= 10

1 <= M <= 10


Example

Input

3 5


Output

*****
*****
*****


Explanation

Self Explanatory
'''

n, m = map(int, input().split())
for i in range(n):
    print('*'*m)