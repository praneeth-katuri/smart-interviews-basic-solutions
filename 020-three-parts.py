'''
Given an array of integers A, print true if we can partition the array into three non-empty subarrays with equal sums.


Input Format

The first line of the input contains an integer N. Second line of input contains an array of size N.


Output Format

Print true if we can partition the array, otherwise false.


Constraints

3 ≤ N ≤ 104

-104 ≤ Ai ≤ 104


Example

Input

10

3 3 6 5 -2 2 5 1 -9 4


Output

true


Explanation

(3 + 3) = (6) = (5 - 2 + 2 + 5 + 1 - 9 + 4) = 6.
'''

n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 3 != 0:
    print("false")
else:
    target = total // 3
    sum1 = 0
    count = 0
    for i in range(n-1):
        sum1 += a[i]

        if sum1 == target:
            count += 1
            sum1 = 0
        
        if count == 2 and i < n - 1:
            print("true")
            break
    else:
        print("false")