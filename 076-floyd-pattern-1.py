'''
Print a right-angled triangle pattern using integers. See the example for more details.


Input Format

The first and only line of input contains a single integer N - the size of the triangle.


Output Format

For the given integer, print the right-angled triangle pattern.


Constraints

1 <= N <= 50


Example

Input

6


Output

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21


Explanation

Self Explanatory
'''

n = int(input())
x = 1
for i in range(0,n):
    for j in range(i+1):
        print(f"{x} ", end= "")
        x += 1
    print()