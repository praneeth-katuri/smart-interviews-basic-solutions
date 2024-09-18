'''
Given a string, compute the length of the longest proper prefix which is same as the suffix of the given string.


Input Format

The input contains a string S, consisting of only lowercase characters.


Output Format

Print the length of the longest proper prefix which is the same as a suffix of the given string.


Constraints

1 <= len(S) <= 100


Example

Input

smartintsmart


Output

5


Explanation

Self Explanatory
'''

s = input()
max_len = 0
for i in range(1, len(s)):
    if s[:i] == s[-i:]:
        max_len = i
print(max_len)