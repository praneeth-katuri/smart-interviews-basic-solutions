'''
Print the area of the rectangle, given its length and breadth.


Input Format

The first and only line of input contains two positive integers L - Length of the rectangle and B - Breadth of the rectangle.


Output Format

Print the area of the rectangle.


Constraints

1 <= L, B <=109


Example

Input

5 8


Output

40


Explanation

Self Explanatory
'''

a, b = map(int, input().split())
print(a*b)