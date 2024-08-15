'''
Given a matrix A of size NxN, interchange the diagonal elements from top to bottom and print the resultant matrix.


Input Format

First line of input contains N - the size of the matrix. It is followed by N lines each containing N integers - elements of the matrix.


Output Format

Print the matrix after interchanging the diagonals.


Constraints

1 <= N <= 100

1 <= A[i][j] <= 104


Example

Input

4

5 6 7 8
13 14 15 16
1 2 3 4
9 10 11 12


Output

8 6 7 5 
13 15 14 16 
1 3 2 4 
12 10 11 9 


Explanation

Self Explanatory
'''

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n -1 -i], matrix[i][i]

for row in matrix:
    print(*row)