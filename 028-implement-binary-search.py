'''
Given a sorted array A of size N, along with an integer target K, implement Binary Search to find the target K in the given array.


Input Format
The first line of input contains an integer N - the size of an array and target K. The second line contains the elements of the array.


Output Format
For each iteration of Binary Search, print the values of low, high, and mid. At the end, if the target K is found in the array, print "True" otherwise, print "False".


Constraints

1 <= N <= 20

1 <= A[i] <= 103


Example

Input 1

9 12

1 4 6 7 10 11 12 20 23


Output 1

0 8 4
5 8 6
True


Input 2

10 21

3 5 8 11 15 17 19 23 26 30

Output 2

0 9 4
5 9 7
5 6 5
6 6 6
False


Explanation

Self Explanatory
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

low, high = 0, n-1
flag = False

while low <= high:
    mid = (low + high) // 2
    print(low, high, mid)
    if arr[mid] == k:
        flag = True
        break
    elif arr[mid] < k:
        low = mid + 1
    else:
        high = mid - 1

if flag:
    print("True")
else:
    print("False")