'''
Print a right-angled triangle pattern. See the example for more details.


Input Format

The first and only line of input contains a single integer N - the size of the triangle.


Output Format

For the given integer, print the right-angled triangle pattern.


Constraints

1 <= N <= 50


Example

Input

5

Output

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15

Explanation

Self Explanatory
'''

n = int(input())
for i in range(1, n+1):
    k = i
    for j in range(1, i+1):
        print(k, end=' ')
        k += n - j
    print()