'''
Given an array of size N, implement Insertion Sort.


Input Format
The first line of input contains an integer N - the size of an array. The second line contains the elements of the array.


Output Format
For each iteration of Insertion Sort, print the array elements.


Constraints

1 <= N <= 20

1 <= A[i] <= 103


Example

Input

5
8 7 1 2 4


Output

7 8 1 2 4
1 7 8 2 4
1 2 7 8 4
1 2 4 7 8


Explanation

Self Explanatory
'''

n = int(input())
arr = list(map(int, input().split()))
for i in range(1,n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    print(*arr)