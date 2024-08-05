'''
Imagine a pilot starting the flight from the ground and flying over a series of different points at different heights. You are given an array, where A[i] represents heights.
Currently, if the pilot is at altitude X at ith point, and if he wants to reach (i+1)th point, his altitude will become X+A[i].
The pilot starts at altitude 0 and wants to find the highest point he can reach during the entire journey. Your task is to print the highest altitude the pilot reaches.


Input Format
The first line of input contains an integer N. The second line of input contains N space-separated integers.


Output Format
Print the highest altitude the pilot can reach.


Constraints

1 <= N <= 1000

-1000 <= A[i] <= 1000


Example

Input

5

-5 1 5 0 -7


Output

1


Explanation

When the pilot started at point 0 his altitude was -5, when he moved to point 1 his altitude became (-5 + 1 = -4), at point 2 his altitude became(-4 + 5 = 1), at point 3

his became altitude remains(1 + 0 = 1), and at point 4 his altitude became (1 + -7 = -6). The maximum altitude that he reached in his journey was 1.
'''

n = int(input())
arr = list(map(int, input().split()))
max_alt = 0
alt = 0

for num in arr:
    alt += num
    max_alt = max(max_alt, alt)

print(max_alt)