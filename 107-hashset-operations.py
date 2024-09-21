'''
Given two arrays of size N and M, insert them into two sets A and B.

Implement the following operations in the same sequential order:

1. Union of A and B: Find the union of A and B, print the elements of the resulting set in sorted order.
2. Intersection of A and B: Find the intersection of A and B, print the elements of the resulting set in sorted order.
3. Symmetric Difference of A and B: Find the symmetric difference of A and B, print the elements of the resulting set in sorted order.
4. Check if A and B are disjoint sets: If yes, print true, otherwise, print false.
5. Check if A is a subset of B: If yes, print true, otherwise, print false.
6. Check if A is a superset of B: If yes, print true, otherwise, print false.


Input Format

The first line of input contains N, the size of array1. The second line of input contains N elements of array1.

The third line of input contains M, the size of array2. The fourth line of input contains M elements of array2.


Output Format

For subset, superset, and disjoint operations print True or False. And for remaining all operations, if resulting set is not empty, print the sorted set separated by spaces, otherwise skip printing the set.


Constraints

1 <= N, M <= 50
1 <= array1[i], array2[i] <= 100


Example

Input

4
9 6 8 7
3
9 9 6


Output

6 7 8 9
6 9
7 8
false
false
true


Explanation

Self Explanatory
'''

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

A = set(arr1)
B = set(arr2)

union = sorted(A | B)
if union:
    print(*union)

intersec = sorted(A & B)
if intersec:
    print(*intersec)

sym_diff = sorted(A ^ B)
if sym_diff:
    print(*sym_diff)

print('true' if A.isdisjoint(B) else "false")

print('true' if A.issubset(B) else 'false')

print('true' if A.issuperset(B) else 'false')