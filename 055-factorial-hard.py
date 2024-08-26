'''
Given a non-negative number - N. Print N!

Input Format

The first and only line of input contains a number - N.


Output Format

Print factorial of N. Since the result can be very large, print result % 1000000007


Constraints

0 <= N <= 106


Examples

Input 1

3


Output 1

6


Input 2

165


Output 2

994387759


Explanation

Self Explanatory


'''

n  = int(input())
MOD = 1000000007

result = 1
for i in range(2, n+1):
    result = (result * i) % MOD

print(result)