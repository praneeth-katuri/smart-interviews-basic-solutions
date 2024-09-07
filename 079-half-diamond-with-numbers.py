'''
Given a value N, print a half diamond pattern with numbers. See examples for more details.

Input Format
First and only line of input contains an integer N.

Output Format
Print the half diamond pattern using numbers.

Constraints
1 <= N <= 100

Example
Input
5

Output
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

Explanation

Self Explanatory
'''

n = int(input())
for i in range(1, n+1):
    print(" ".join(str(x) for x in range(1,i+1)))

for i in range(n-1, 0, -1):
    print(" ".join(str(x) for x in range(1,i+1)))