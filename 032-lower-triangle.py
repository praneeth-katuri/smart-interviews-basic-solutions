'''
Given a square matrix of size N × N, find the sum of its lower triangle elements.


Input Format

The first line of input contains N - the size of the matrix. It is followed by N lines each containing N integers - elements of the matrix.


Output Format

Print the sum of the lower triangle of the matrix.


Constraints

1 <= N <= 100

-105 <= ar[i] <= 105


Example

Input

3

5 9 -2

-3 4 1

2 6 1


Output

15


Explanation

The sum of the lower triangle matrix is 5 - 3 + 4 + 2 + 6 + 1 = 15.
'''

matrix = []
lt_sum = 0
for _ in range(int(input())):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(_+1):
        lt_sum += row[j]
print(lt_sum)