'''
Given a quadratic equation in the form ax2 + bx + c, (only the values of a, b and c are provided). Find the roots of the equation.

Note: Display the values with precision up to two decimal places, and for imaginary roots of the form (x + iy) or (x - iy), print "Imaginary Roots".


Input Format

First and only line of input contains three integers a, b, c separated by spaces.


Output Format

Print the roots of the quadratic equation separated by spaces.


Constraints

-1000 <= a, b, c <= 1000


Examples

Input 1

1 -2 1


Output 1

1.00 1.00


Input 2

1 7 12


Output 2

-3.00 -4.00


Input 3

1 1 1


Output 3

Imaginary Roots


Explanation

Example 1: Roots are real and equal, which are (1,1)

Example 2: Roots are real and distinct, which are (-3,4)

Example 3: Roots are imaginary, which are (-0.5 + i0.866025, -0.5 - i0.866025)
'''

a, b, c = map(int, input().split())
discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print("Imaginary Roots")
elif discriminant > 0:
    root1 = (-b + (discriminant ** 0.5))/(2 * a)
    root2 = (-b - (discriminant ** 0.5))/(2 *a)
    print(f"{root1:.2f} {root2:.2f}")
else:
    root1 = -b/(2*a)
    print(f"{root1:.2f} {root1:.2f}")