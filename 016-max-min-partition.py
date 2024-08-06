'''
Given an array D of positive integers, your goal is to divide D into two separate arrays, E and F, under the following conditions:

--> Each element in array D must belong to either array E or array F
--> Both arrays E and F are non-empty
--> The objective is to minimize the partition's value, calculated as the absolute difference between the maximum value of array E (denoted as max(E)) and the minimum value of array F (denoted as min(F))

Print the resulting integer that represents the value of this partition.

Input Format

The first line of input contains N. The second line of input contains an array of size N.


Output Format

Print the minimized partition value.


Constraints

2 ≤ N ≤ 104
1 ≤ Di ≤ 109


Example

Input

6

7 1 14 16 30 4


Output

2

Explanation

We can partition the array D into E = [7, 1, 14, 4] and F = [16, 30].

The maximum element of the array E is equal to 14.
The minimum element of the array F is equal to 16.
The value of the partition is |14 - 16| = 2. It can be proven that 2 is the minimum value out of all the partitions.
'''

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_part = float('inf')

for i in range(1, n):
    max_e = arr[i-1]
    min_f = arr[i]
    part_val = abs(max_e -min_f)
    min_part = min(min_part, part_val)
print(min_part)