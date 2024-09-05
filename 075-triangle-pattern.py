'''
Given a value N, print a right-angled triangle pattern. See examples for more details.

Input Format
First and only line of input contains an integer N.

Output Format
Print the right angled triangle pattern.

Constraints
1 <= N <= 100

Example
Input
5

Output
*
* *
* * *
* * * *
* * * * *

Explanation

Self Explanatory
'''

n = int(input())
for _ in range(1,n+1):
    print('* '*_)