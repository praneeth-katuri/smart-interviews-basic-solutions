'''
Given a matrix of size N x M, print whether it is a sparse matrix or not.

Please note that if a matrix contains 0 in more than half of its cells, then it is called a sparse matrix.


Input Format

The first line of input contains N, M - the size of the matrix, followed by N lines each containing M integers - elements of the matrix.


Output Format

Print "Yes" if the given matrix is a sparse matrix, otherwise print "No".


Constraints

1 <= N, M <= 100

0 <= ar[i] <= 109


Example

Input

2 3

5 0 0
0 8 0

Output

Yes


Explanation

Self Explanatory
'''

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
total_ele = n * m
zero_count = 0
for row in matrix:
    zero_count += row.count(0)

if zero_count > total_ele // 2:
    print("Yes")
else:
    print("No")
