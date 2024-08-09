'''
Given an array of size N, implement Bubble Sort.

Input Format
The first line of input contains an integer N - the size of an array. The second line contains the elements of the array.


Output Format
For each iteration of Bubble Sort, print the array elements.


Constraints

1 <= N <= 20

1 <= A[i] <= 103


Example

Input

6
5 8 10 15 3 6

Output

5 8 10 3 6 15
5 8 3 6 10 15
5 3 6 8 10 15
3 5 6 8 10 15
3 5 6 8 10 15


Explanation

Self Explanatory
'''

n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1):
    flag = False
    for j in range(n - 1 - i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag = True
    print(*arr)