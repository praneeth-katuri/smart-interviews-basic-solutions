'''
Given an array of integers, search a given key in the array using linear search.

Note: Do not use any inbuilt functions / libraries for your main logic.


Input Format
The first line of input contains two integers N and K. N is the size of the array and K is the key. The second line contains the elements of the array.


Output Format
If the key is found, print the index of the array, otherwise print -1.


Constraints

1 <= N <= 102

0 <= ar[i] <= 109


Example

Input

5 15

-2 -19 8 15 4


Output

3


Explanation

Self Explanatory
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k in arr:
        print(f"{arr.index(k)}")
else:
        print(-1)