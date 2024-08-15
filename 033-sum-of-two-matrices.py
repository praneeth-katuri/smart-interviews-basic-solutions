'''
Given two matrices A and B each of size N x M, print the sum of the matrices (A + B).


Note:
Try solving it by declaring only a single matrix.


Input Format
The first line of input contains N, M - the size of the matrices. It's followed by 2*N lines, each containing M integers - elements of the matrices. The first N lines are for matrix A and the next N lines are for matrix B.


Output Format

Print the sum of the 2 given matrices (A + B).


Constraints

1 <= N, M <= 100

-109 <= ar[i] <= 109


Example

Input

2 3

5 -1 3

19 8 4

4 5 -6

1 -2 12


Output

9 4 -3

20 6 16


Explanation

Self Explanatory
'''

N, M = map(int, input().split())
sum_matrix = [[0] * M for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        sum_matrix[i][j] += row[j]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        sum_matrix[i][j] += row[j]

for row in sum_matrix:
    print(" ".join(map(str, row)))
