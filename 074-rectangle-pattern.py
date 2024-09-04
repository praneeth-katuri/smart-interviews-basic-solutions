'''
Print rectangle pattern. See the example for more details.


Input Format

The first and only line of input contains a single integer N.


Output Format

For the given integer, print a rectangle pattern as shown in the example.


Constraints

1 <= N <= 50


Example

Input

5

Output

5432*
543*1
54*21
5*321
*4321

Explanation

Self Explanatory


'''

n = int(input())
val = 1
for i in range(n):
    for j in range(n, 0, -1):
        if j == val:
            print("*", end= '')
        else:
            print(j,end='')
    val += 1
    print()