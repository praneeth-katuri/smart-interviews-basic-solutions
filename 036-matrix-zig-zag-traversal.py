'''
Given a matrix of size N x M, print the matrix in zig-zag order. Refer example for more details.

Input Format

The first line of input contains N, M - the size of the matrix. It is followed by N lines each containing M integers - elements of the matrix.


Output Format

Print the matrix elements in zig-zag order.


Constraints

1 <= N, M <= 100

-106 <= mat[i][j] <= 106


Example

Input

3 3

5 9 -2
-3 4 1
2 6 1


Output

5 9 -2 1 4 -3 2 6 1


Explanation

Self Explanatory
'''

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            result.append(matrix[i][j])
    else:
        for j in range(m -1, -1, -1):
            result.append(matrix[i][j])
print(*result)