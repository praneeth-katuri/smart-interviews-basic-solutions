'''
Given a matrix of size N x M, print the transpose of the matrix.

Input Format

The first line of input contains N, M - the size of the matrix. It is followed by N lines each containing M integers - elements of the matrix.

Output Format

Print the transpose of the given matrix.


Constraints

1 <= N, M <= 100

-109 <= ar[i] <= 109


Example

Input

2 2
5 -1
19 8


Output

5 19

-1 8


Explanation
Self Explanatory
'''

n, m = map(int, input().split())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for j in range(m):
    for i in range(n):
        print(a[i][j], end=" ")
    print()