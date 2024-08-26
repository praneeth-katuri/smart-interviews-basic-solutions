'''
Given a number N, find a number X. On subtracting X from N, N-X should be a power of 2. Find the minimum value of X.


Input Format

The first and only line of input contains an integer N.


Output Format

Print the value X.


Constraints

2 <= N <= 109


Example

Input

10


Output

2


Explanation

N = 10

If we subtract X = 2 from N = 10, N - X = 8 is a power of 2.
'''

n = int(input())
min_x = float('inf')

p = 1
while p <= n:
    x = n - p
    if x >= 0:
        min_x = min(min_x, x)
    p *= 2
print(min_x)