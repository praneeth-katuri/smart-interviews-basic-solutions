'''
A balanced string is one that contains an equal quantity of 'L' and 'R' characters. Given a balanced string S, your task is to split it into some number of substrings such that each substring is also balanced. Output the maximum number of balanced strings you can obtain through this splitting process.


Input Format

The first and only line of input contains string S.


Output Format

Print the maximum number of balanced strings you can obtain with the splitting process.


Constraints

2 ≤ len(A) ≤ 1000


Example

Input

LRRLLLLRRLRR

Output

3


Explanation

The string 'LRLLLRRLRR' can be split into three substrings: "LR", "RL" and "LLLRRLRR," each containing the same number of 'L' and 'R' characters.
'''

s = input()
even = 0
count = 0
for char in s:
    if char == 'L':
        even += 1
    if char == 'R':
        even -= 1
    
    if even == 0:
        count += 1
print(count)