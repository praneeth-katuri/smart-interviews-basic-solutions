'''
For an Arithmetic Progression series with a given first term (a), common difference (d), and an integer N, determine the Nth term of the series.


Input Format

First and only line of input contains 3 variables a, d and N.


Output Format

Print the Nth term of the AP series.


Constraints

1 <= a, d, N <= 103


Example

Input

2 1 5


Output

6


Explanation

Self Explanatory
'''

a, d, n = map(int, input().split())
nthTerm = a + (n-1) * d;
print(nthTerm)