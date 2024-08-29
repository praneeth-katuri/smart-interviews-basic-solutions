'''
Given an integer N, check whether it is a Harshad number or not.

Note that a Harshad number is an integer, that is divisible by the sum of its digits.


Input

The first and only line of input contains a integer - N.


Output

Print "Yes" if the number is Harshad number, "No" otherwise.


Constraints

1 <= N <= 109


Example

Input

18


Output

Yes


Explanation

18 / (1 + 8) = 2

As 18 is divisible by the sum of its digits, it is a Harshad number.
'''

n = input()
m = int(n)
tmp = m
s =0
while tmp != 0:
    s += tmp % 10
    tmp = tmp // 10

if m%s == 0:
    print("Yes")
else:
    print("No")