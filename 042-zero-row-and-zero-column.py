'''
Given a matrix A of size N x M. Elements of the matrix are either 0 or 1. If A[i][j] = 0, set all the elements in the ith row and jth column to 0. Print the resultant matrix.


Input Format

The first line of input contains N, M - the size of the matrix A. It is followed by N lines each containing M integers - elements of the matrix.


Output Format

Print the resultant matrix.


Constraints

1 <= N, M <= 100

A[i][j] ∈ {0,1}


Example

Input

4 5

0 1 1 0 1 
1 1 1 1 1 
1 1 0 1 1 
1 1 1 1 1 


Output

0 0 0 0 0 
0 1 0 0 1 
0 0 0 0 0 
0 1 0 0 1 


Explanation

Self Explanatory
'''

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
zero_rows = set()
zero_cols = set()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero_cols.add(j)
            zero_rows.add(i)

for i in range(n):
    for j in range(m):
        if i in zero_rows or j in zero_cols:
            matrix[i][j] = 0

for row in matrix:
    print(*row)