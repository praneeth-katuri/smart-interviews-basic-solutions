'''
Given positive integer - N, print the sum of the first N natural numbers.


Input Format

The first and only line of input contains a positive integer - N.


Output Format

Print the sum of the first N natural numbers.


Constraints

1 <= N <= 104


Example

Input

4


Output

10


Explanation

Self Explanatory
'''

n = int(input())
print((n * (n+1)//2))