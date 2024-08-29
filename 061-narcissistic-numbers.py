'''
Given an integer N, check whether it is a Narcissistic number or not.

Note that a Narcissistic number is a number that is the sum of its own digits each raised to the power of the number of digits


Input Format

The first and only line of input contains an integer - N.


Output Format

Print "Yes" if the number is Narcissistic number, "No" otherwise.


Constraints

0 <= N <= 106


Example

Input

8208


Output

Yes


Explanation

84 + 24 + 04 + 84 = 8208
'''


n = int(input())

def order(x):
  n = 0
  while x != 0:
    x = x//10
    n += 1
  return n

def isNarcissistic(x):
  n = order(x)
  sum1 = 0
  temp = x
  while temp != 0:
    r = temp % 10
    sum1 += r ** n
    temp //= 10

  if sum1 == x:
    return "Yes"
  else:
    return "No"

print(isNarcissistic(n))