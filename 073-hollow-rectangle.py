'''
Print a hollow rectangle pattern using '*'. See the example for more details.

Input Format

The input contains two integers W - width of the rectangle and L - length of the rectangle.

Output Format

For the given integers W and L, print the hollow rectangle pattern.


Constraints

2 <= W <= 50

2 <= L <= 50


Example

Input

5 4


Output

*****
*   *
*   *
*****

Explanation

Self Explanatory
'''

w, l = map(int, input().split())
print('*' * w)
for _ in range(l - 2):
    print('*'," "*(w-4),'*')
print('*'*w)