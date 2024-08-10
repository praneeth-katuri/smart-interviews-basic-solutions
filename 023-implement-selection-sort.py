'''
Given an array of size N having unique elements, implement Selection Sort.

Note: Implement Selection Sort by selecting smallest element at every step.


Input Format
The first line of input contains an integer N - the size of an array. The second line contains the elements of the array.


Output Format
For each iteration of Selection Sort, print the array elements.


Constraints

1 <= N <= 20

1 <= A[i] <= 103


Example

Input

6
5 8 10 15 3 6


Output

3 8 10 15 5 6
3 5 10 15 8 6
3 5 6 15 8 10
3 5 6 8 15 10
3 5 6 8 10 15


Explanation

Self Explanatory
'''

n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print(*arr)