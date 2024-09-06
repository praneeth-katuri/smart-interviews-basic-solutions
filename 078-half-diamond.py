'''
Print half diamond pattern using '*'. See the example for more details.

Input Format

The first and only line of input contains a single integer N.

Output Format

For the given integer, print the half-diamond pattern.

Constraints

1 <= N <= 50


Example

Input

5

Output

*
**
***
****
*****
****
***
**
*


Explanation

Self Explanatory
'''

n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

for i in range(1, n):
    for j in range(n-1, i-1, -1):
        print("*", end="")
    print()