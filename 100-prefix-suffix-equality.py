'''
Given strings S and T. Print "Yes", if T is both a prefix and a suffix of S, otherwise "No".


Input Format

First and only line of input contains two strings separated by a space.


Output Format

Print "Yes", if T is both a prefix and a suffix of S, otherwise "No".


Constraints

1 <= len(S), len(T) <= 1000

'a' <= S[i], T[i] <= 'z'


Example

Input

smartinterviewssmart smart


Output

Yes


Explanation

Self Explanatory
'''

s, t = input().split()
count = 0
for i in range(len(t)):
    if s[i] == t[i] and s[-i-1] == t[-i-1]:
        count += 1
if count == len(t):
    print("Yes")
else:
    print("No")