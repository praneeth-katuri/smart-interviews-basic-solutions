'''
Given an array A of size N, find the minimum cost to convert it to a ternary array B. A ternary array can only have 0 or 1 or 2. After conversion, ensure that A[i] != B[i]. The cost of converting A[i] to B[i] is | A[i] - B[i] |.

Input Format

The first line of input contains a single integer N - the size of the array and the second line contains array elements.

Output Format

Print the minimum cost to convert array A to B.


Constraints

1 <= N <= 10000

-100000 <= A[i] <= 100000


Example

Input

5

1 -1 2 0 5


Output

7


Explanation

Given A = {1, -1, 2, 0, 5} can be converted to B = {2, 0, 1, 1, 2}, with a cost of |1-2| + |-1-0| + |2-1| + |0-1| + |5-2| = 1 + 1 + 1 + 1 + 3 = 7.
'''

n = int(input())
A = list(map(int, input().split()))

total_cost = 0

for a in A:
    if a < 0:
        total_cost += abs(a-0)
    elif a == 0:
        total_cost += min(abs(a-1), abs(a-2))
    elif a == 1:
        total_cost += min(abs(a-0), abs(a-2))
    elif a == 2:
        total_cost += min(abs(a-0), abs(a-1))
    else:
        total_cost += abs(a-2)

print(total_cost)