'''
You are given an N x M binary matrix called "image". You need to perform the following operations on the matrix (in order) and return the resulting image:

1. Flip the image horizontally: This involves reversing the order of elements in each row of the matrix. For example, [1,0,1,0,0,0] becomes [0,0,0,1,0,1]
2. Invert the image: This involves replacing 0s with 1s and 1s with 0s in the entire matrix. For example, [0,0,0,1,0,1] becomes [1,1,1,0,1,0]

Input Format

Line of input contains N - number of rows and M - number of columns. The next N lines contains M integers each denoting the elements of the matrix image.


Output Format

You have to print the resultant matrix image.


Constraints

1 <= N <=100

1 <= M <=100


Example

Input

2 2
1 0
0 1


Output

1 0
0 1


Explanation

Self Explanatory
'''

n, m = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    image[i] = image[i][::-1]

for i in range(n):
    image[i] = [1 - j for j in image[i]]

for row in image:
    print(*row)