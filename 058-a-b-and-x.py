'''
You are given two numbers A and B along with an integer X. In one operation you can do one of the following:

Set A = A + X and B = B - X

Set A = A - X and B = B + X

Determine if you can make A and B equal after applying the operation any number of times (possibly zero).


Input Format

The first and only line of input contains three integers A, B, and X separated by a space.


Output Format

For each test case, print YES if you can make A and B equal, otherwise NO.


Constraints

1 <= A, B, X <= 109


Examples

Input 1

6 8 1


Output 1

YES


Input 2

15 16 2


Output 2

NO


Explanation

Example 1: The initial values of (A, B) are (6,8). We can perform the following operation.

A = A + X = 6 + 1 = 7 and B = B - X = 8 - 1 = 7

A and B are equal, print YES.


Example 2: It can be proven that we cannot make A equal to B using the given operations.
'''

a, b, x = map(int, input().split())
diff = abs(a-b)

if diff % (2*x) == 0:
    print("YES")
else:
    print("NO")