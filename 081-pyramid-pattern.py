'''
Print pyramid pattern using '*'. See the example for more details.


Input Format

The first and only line of input contains a single integer N - the size of the pyramid.


Output Format

For the given integer, print the pyramid pattern.


Constraints

1 <= N <= 50


Example

Input

5

Output

    *
   ***
  *****
 *******
*********

Explanation

Self Explanatory
'''

n = int(input())
c = 0
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(end=" ")
    while c != 2*i-1:
        print("*",end="")
        c += 1
    c = 0
    print()