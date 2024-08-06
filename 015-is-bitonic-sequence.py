'''
Given an array of integers A, print true if and only if it is a valid array. A is a valid array if and only if there exists some i with 0 < i < A.length - 1 such that: A[0] < A[1] < ... < A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1].

Input Format

The first line of the input contains N. Second line of input contains an array of size N.

Output Format

Print true if and only if it is a valid array, otherwise print false.


Constraints

3 ≤ N ≤ 104

0 ≤ Ai ≤ 104


Example

Input

4

0 3 2 1


Output

true


Explanation

ar = [0, 3, 2, 1]
idx = 0 1 2 3
So if we take i=1, then we have ar[0] < ar[1] > ar[2] > ar[3]
0 < 3 > 2 > 1
'''

n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print('false')
    exit()

i = 0
while i + 1 < n and a[i] < a[i+1]:
    i += 1

if i == 0 or i == n-1:
    print('false')
    exit()

while i + 1 < n and a[i] > a[i+1]:
    i += 1

if i == n-1:
    print('true')
else:
    print('false')