'''
Given a non-negative integer - N, print the sum of digits of the given number.


Input Format

The first and only line of input contains a non-negative integer N.


Output Format

Print the sum of the digits of the given number.


Constraints

1 <= length(N) <= 103


Example

Input

164


Output

11


Explanation

1 + 6 + 4 = 11
'''

n = int(input())
sum1 = 0

while n != 0:
    sum1 += n % 10
    n //= 10

print(sum1)