'''
Given a matrix of size N x M, print column-wise sum, separated by a newline.


Input Format

The first line of input contains N, M - the size of the matrix, followed by N lines each containing M integers - elements of the matrix.


Output Format

Print the column-wise sum of the matrix, separated by newline.


Constraints

1 <= N, M <= 100

-100 <= ar[i] <= 100


Example

Input

2 2

5 -1

19 8


Output

24

7


Explanation

Self Explanatory
'''

n, m = map(int, input().split())
column_sums = [0] * m
for _ in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        column_sums[j] += row[j]
print(*column_sums, sep='\n')