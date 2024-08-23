'''
Given a number N, reverse the number.

Input Format

The first and only line of input contains a integer - N.


Output Format

Print the reversed number.


Constraints

-109 <= N <= 109


Example

Input

1344


Output

4431

Explanation

Self Explanatory
'''

n = int(input())
flag = 0
if n < 0:
    flag = 1
    n = abs(n)
reverse = 0
while n != 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if flag == 1:
    print(-reverse)
else:
    print(reverse)