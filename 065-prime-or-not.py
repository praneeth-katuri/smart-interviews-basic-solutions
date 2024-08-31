'''
Given a positive integer - N, check whether the number is prime or not.


Input Format

The first and only line of input contains an integer - N.


Output Format

Print "Yes" if the number is prime, "No" otherwise.


Constraints

1 <= N <= 108


Example

Input

11


Output

Yes


Explanation

Self Explanatory
'''

n = int(input())

def check_prime(n):
    if n <= 1:
        return "No"
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "No"
    return "Yes"

print(check_prime(n))