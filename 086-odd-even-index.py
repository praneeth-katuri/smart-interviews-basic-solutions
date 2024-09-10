'''
Given a string, print all the letters present at the odd index, followed by the letters present at the even index.


Input Format

The input contains a string S, consisting of ASCII characters.


Output Format

Print letters present at odd index, followed by the letters present at even index.


Constraints

1 <= len(S) <= 100


Example

Input

afdg5tg


Output

fgtad5g


Explanation

Self Explanatory
'''

s = input()
for i in range(len(s)):
    if i % 2 == 1:
        print(s[i], end = "")

for j in range(len(s)):
    if j % 2 == 0:
        print(s[j],end ="")