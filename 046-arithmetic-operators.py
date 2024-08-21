'''
Given two integers A and B. Print the sum, difference, product, division, and remainder for the corresponding values of A and B.


Input Format

First and only line of input contains two integers - A and B.


Output Format

Print the sum, difference, product, division, and remainder for the corresponding values of A and B. Refer the given example.

Constraints

1 <= A, B <= 1000


Example

Input

12 5


Output

Sum: 17
Difference: 7
Product: 60
Division: 2
Remainder: 2


Explanation

Self Explanatory
'''

a,b = map(int, input().split())
print("Sum:",a+b)
print("Difference:",a-b)
print("Product:", a*b)
print("Division:",a//b)
print("Remainder:", a%b)