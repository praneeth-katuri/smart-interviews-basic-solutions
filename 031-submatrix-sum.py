'''
Given a matrix of size N x N and four integers (i, j, k, l), calculate the sum of the sub-matrix from (i, j) to (k, l).


Input Format

The first line of input contains an integer N. Second line of input contains four integers i, j, k and l. It's followed by N lines each containing N integers - elements of the matrix.


Output Format

Print the sum of the sub-matrix from (i, j) to (k,l).


Constraints

1 <= N <= 100

0 <= i <= k < N

0 <= j <= l < N

1 <= ar[i][j] <= 100


Example

Input

3

1 1 2 2

1 2 3

4 5 6

7 8 9


Output

28


Explanation

Sum of elements from {1,1} to {2, 2} is (5+6+8+9) = 28.
'''

n = int(input())
i, j, k, l = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

sum_sub = 0
for row in range(i, k+1):
    for col in range(j, l+1):
        sum_sub += matrix[row][col]
print(sum_sub)