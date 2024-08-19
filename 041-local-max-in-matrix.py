'''
Given an integer matrix C with dimensions N × N. Construct a new integer matrix D of size (N - 2) × (N - 2) such that each element D[i][j] represents the maximum value within a 3 × 3 submatrix of C, where the center of the submatrix is located at row i + 1 and column j + 1 in matrix C. We aim to identify the highest value within every continuous 3 × 3 submatrix within C. Print the resulting matrix D.


Input Format

The first line of input contains an integer N. For the next N lines, each line contains N elements separated by space.


Output Format

Print the generated matrix.

Constraints

3 ≤ N ≤ 100

-1000 ≤ Cij ≤ 1000

Example

Input

4

12 9 8 40
5 20 2 6
8 14 6 30
6 2 25 2


Output

20 40
25 30

Explanation

Self Explanatory
'''

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
D = [[0] * (N-2) for _ in range(N-2)]
for i in range(1, N-1):
    for j in range(1, N-1):
        max_val = -float('inf')
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                max_val = max(max_val, C[x][y])
        
        D[i-1][j-1] = max_val

for row in D:
    print(*row)