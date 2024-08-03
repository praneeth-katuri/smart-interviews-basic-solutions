'''
Print unique elements of the array in the same order as they appear in the input.

Note:
Do not use any inbuilt functions / libraries for your main logic.

Input Format

The first line of input contains the size of the array - N and the second line contains the elements of the array.

Output Format

Print unique elements from the given array.


Constraints

1 <= N <= 100

0 <= ar[i] <= 109


Example

Input

7

5 4 10 9 21 4 10


Output

5 9 21

Explanation

Self Explanatory
'''

n = int(input())
arr = list(map(int, input().split()))
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

result = []
for num in arr:
    if freq[num] == 1:
        result.append(num)

print(*result)