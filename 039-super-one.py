'''
Given a matrix of 0’s and 1’s, check if there exists a Super One. Please note that a Super One is a 1, which is surrounded by 0 on all 8 sides.


Input Format

The first line of input contains N, M - the size of the matrix. It's followed by N lines each containing M integers - elements of the matrix.


Output Format

Print "Yes" if the matrix contains Super One, otherwise print "No".

Constraints

1 <= N, M <= 100

0 <= ar[i] <= 1


Example

Input

4 4

1 0 0 0
0 0 0 1
0 1 0 0
0 0 0 0


Output

Yes


Explanation

There's one occurrence of Super One in the matrix at [2,1]. Value 1 at index [0,0] and Value 1 at index [1,3] are not Super One's because they are not surrounded by eight 0's.
'''

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

if N < 3 or M < 3:
    print("No")
else:
    directions = [(-1, -1), (-1, 0), (-1, -1), (0, -1), (0, 1), (1, 1), (1, 0),(1, 1)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if matrix[i][j] == 1:
                is_super = True
                for dx, dy in directions:
                    if matrix[i + dx][j + dy] != 0:
                        is_super = False
                if is_super:
                    print('Yes')
                    exit()
    print('No')