'''
Given a value N, print the Pascal's Triangle pattern.


Input Format

The first and only line of input contains an integer N.


Output Format

For the given input, print the Pascal's Triangle pattern.


Constraints

1 ≤ N ≤ 30


Example

Input

10


Output

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1


Explanation

Self Explanatory
'''

n = int(input())
pr = [1]
print("1")
for i in range(1, n):
    cr = [1]
    for j in range(1, i):
        cr.append(pr[j-1] + pr[j])
    cr.append(1)
    print(*cr)
    pr = cr