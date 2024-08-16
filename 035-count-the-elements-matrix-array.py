'''
You are given a matrix and an array. For each row of the given matrix, for each element of that row, check if it is present in the given array. Print the count of elements present for every row.


Input Format

The first line of input contains N, M - the size of the matrix. It is followed by N lines each containing M integers - elements of the matrix. The next line of the input contains the A - the size of the array. The next line of the input contains the array elements.


Output Format

For each row, print the count of the number of elements present, separated by a new line.


Constraints

1 <= N, M, A <= 100

-100 <= mat[i][j], ar[i] <= 100


Example

Input

3 4
5 9 -2 2
-3 4 1 9
2 -2 1 -2
5
5 1 -2 2 6


Output

3
1
4


Explanation

The first row of the matrix is (5 9 -2 2), out of this, 3 elements (5 -2 2), except 9, are present in the given array (5 1 -2 2 6)

The second row of the matrix is (-3 4 1 9), out of this, only 1 is present in the given array (5 1 -2 2 6)

The third row of the matrix is (2 -2 1 -2), all the 4 elements are present in the given array (5 1 -2 2 6)
'''

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

a = int(input())
arr = set(map(int, input().split()))

for row in matrix:
    count = sum(1 for element in row if element in arr)
    print(count)