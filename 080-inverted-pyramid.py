'''
Print a hollow half-inverted pyramid pattern using '*'. See the example for more details.


Input Format

The first and only line of input contains a single integer N.


Output Format

For the given integer, print hollow half-inverted pyramid pattern.


Constraints

1 <= N <= 50


Example

Input

5


Output

* * * * *
*     *
*   *
* *
*

Explanation

Self Explanatory
'''

n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        if i == n:
            print('*', end=' ')
        else:
            if j == 0 or j == i-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()