'''
Given a matrix of size N x M, print row-wise sum, separated by a newline.


Note:
Try to solve this without declaring / storing the matrix.

Input Format
The first line of input contains N, M - the size of the matrix, followed by N lines each containing M integers - elements of the matrix.

Output Format
Print the row-wise sum of the matrix, separated by a newline.


Constraints

1 <= N, M <= 100

-100 <= ar[i] <= 100


Example

Input

2 3

5 -1 3

19 8 -5


Output

7

22


Explanation

Self Explanatory
'''

n, m = map(int, input().split())

for i in range(n):
    row_sum = sum(map(int, input().split()))
    print(row_sum)