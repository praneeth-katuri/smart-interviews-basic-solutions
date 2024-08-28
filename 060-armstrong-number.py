'''
Given an integer N, check whether it's an Armstrong number or not.

Note that an Armstrong number is a number that is equal to the sum of cubes of its digits.


Input Format

The first and only line of input contains an integer - N.


Output Format

Print "Yes" if the number is Armstrong number, "No" otherwise.


Constraints

0 <= N <= 109


Example

Input

153


Output

Yes


Explanation

13 + 53 + 33 = 153
'''

n = int(input())
org = n
sum_of_cubes = 0

while n > 0:
    digit = n % 10
    sum_of_cubes += digit ** 3
    n = n // 10

if sum_of_cubes == org:
    print("Yes")
else:
    print("No")