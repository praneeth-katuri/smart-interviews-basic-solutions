'''
Given the length of 3 sides of a triangle, check whether the triangle is valid or not.


Input Format

The first and only line of input contains three integers A, B, C - Sides of the triangle.


Output Format

Print "Yes" if you can construct a triangle with the given three sides, "No" otherwise.


Constraints

1 <= A, B, C <= 109


Example

Input

4 3 5


Output

Yes


Explanation

Self Explanatory
'''

a,b,c = map(int, input().split())
if a+b>c and b+c>a and c+a>b:
    print("Yes")
else:
    print("No")