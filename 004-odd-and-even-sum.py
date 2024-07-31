'''
Given an array of size N. Print the sum of odd and even numbers separated by a space.

Input Format
The first line of input contains N - the size of the array and the second line contains elements of the array.

Output Format
Print the sum of odd elements followed by sum of even elements.

Constraints
1 <= N <= 103
1 <= ar[i] <= 106

Example
Input
5
4 6 9 2 5

Output
14 12

Explanation

Self Explanatory

'''

n = int(input())
arr = list(map(int, input().split()))

even_sum = sum(i for i in arr if i % 2 == 0)
odd_sum = sum(i for i in arr if i % 2 != 0)

print(odd_sum, even_sum)