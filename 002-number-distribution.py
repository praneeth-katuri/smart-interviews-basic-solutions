'''
Print the count of the occurrences of positive integers, negative integers, and zeroes in the given array.


Input Format

The first line of the input contains an integer N - size of the array, second line of input contains an array elements of the array.


Output Format

Print the frequencies of zeroes, positives elements and negative elements.


Constraints

1 <= N <= 104

-103 <= arr[i] <= 103


Example

Input

10

120 0 -9 89 68 -982 91 -54 -12 -139


Output

1 4 5


Explanation

Self Explanatory
'''

n = int(input())
arr = list(map(int, input().split()))

zero_count = sum(1 for num in arr if num == 0)
positive_count = sum(1 for num in arr if num > 0)
negative_count = sum(1 for num in arr if num < 0)

print(zero_count, positive_count, negative_count)