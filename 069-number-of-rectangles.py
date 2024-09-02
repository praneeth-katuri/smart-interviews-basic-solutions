'''
Vikram has a collection of N squares with a side length of 1. Print the number of different rectangles that can be formed using these squares.

Input Format
Print the number of different rectangles that can be formed using these squares.

Output Format
Print the number of different rectangles that can be formed using these squares.

Constraints
1 ≤ N ≤ 100

Example
Input
6

Output
8

Explanation

We can create different rectangles of sizes 1×1, 1×2, 1×3, 1×4, 1×5, 1×6, 2×2, 2×3.
'''

n = int(input())
count = 0
for i in range(1, int(n**0.5)+1):
    for j in range(i, n+1):
        if i*j <= n:
            count += 1
        else:
            break
print(count)