'''
Given a sorted array A, containing N integers. Calculate and print their Mean, Median and Mode.

1. For both the Mean and Median, display the values with precision up to two decimal places.

2. Print the first Mode that you encounter from the left hand side.

Input Format

First line of input contains integer N - the size of the array. Second line of input contains N integers - elements of the array A.


Output Format

Print Mean, Median and Mode, separated by spaces.


Constraints

1 <= N <=104

0 <= A[i] <=100


Example

Input

8

1 2 3 4 5 5 6 6

Output

4.00 4.50 5

Explanation:

The Mean is 32 / 8 = 4.00 [rounded to 2 decimals]

The Median is (4+5) / 2 = 4.50

For the given example, {5, 6} represents the Mode of the array, we'll print 5 as it's the first Mode encountered.
'''

length = int(input())
arr = list(map(int, input().split()))
sum_ele = sum(arr)
freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
max_count = max(freq.values())
mode = min(k for k, v in freq.items() if v == max_count)
arr.sort()
median = (arr[length//2] + arr[(length-1)//2]) / 2 if length % 2 == 0 else arr[length//2]
mean = sum_ele /length

print(f"{mean:.2f} {median:.2f} {mode}")