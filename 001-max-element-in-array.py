'''
Find the maximum element from the given array of integers.


Input Format
The first line of input contains N - the size of the array and the second line contains the elements of the array.


Output Format
Print the maximum element of the given array.


Constraints

1 <= N <= 103
-109 <= ar[i] <= 109


Example

Input

5

-2 -19 8 15 4

Output

15


Explanation

Self Explanatory
'''

n = int(input())
print(max(map(int, input().split())))