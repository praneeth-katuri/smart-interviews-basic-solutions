'''
Given two strings A and B of length N, check if string A is a rotation of string B.


Input Format

The first line of input contains N - the length of the strings. The second line contains A and B separated by a space.


Output Format

Print "yes" if A is a rotation of B, otherwise "no".


Constraints

1 <= N <= 500

'a' <= A[i], B[i] <= 'z'


Example

Input

5

hello lohel


Output

yes


Explanation

Self Explanatory
'''

n = int(input())
a, b = input().split()
if len(a) != len(b):
    print("no")

if a in (b+b):
    print("yes")
else:
    print("no")