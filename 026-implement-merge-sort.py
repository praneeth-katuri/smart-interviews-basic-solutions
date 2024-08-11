'''
Given an array of size N, implement Merge sort.


Input Format
The first line of input contains an integer N - the size of an array. The second line contains the elements of the array.


Output Format
For each merge call of Merge Sort, print the array elements.


Constraints

1 <= N <= 20

1 <= A[i] <= 103


Example

Input

6
5 1 3 15 10 4


Output

1 5 3 15 10 4 
1 3 5 15 10 4 
1 3 5 10 15 4 
1 3 5 4 10 15 
1 3 4 5 10 15 


Explanation

Self Explanatory
'''

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid+1, end)
        merge(arr, start, mid, end)
        print(*arr)

def merge(arr, start, mid, end):
    temp = []
    left_idx = start
    right_idx = mid+1

    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] <= arr[right_idx]:
            temp.append(arr[left_idx])
            left_idx += 1
        else:
            temp.append(arr[right_idx])
            right_idx += 1
    
    while left_idx <= mid:
        temp.append(arr[left_idx])
        left_idx += 1
    
    while right_idx <= end:
        temp.append(arr[right_idx])
        right_idx += 1
    
    for i in range(len(temp)):
        arr[start+i] = temp[i]

n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr, 0, n-1)