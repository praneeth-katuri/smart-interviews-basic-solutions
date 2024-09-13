'''
Given a string, check if it contains only digits.


Input Format

The input contains a string S, consisting of ASCII characters.


Output Format

Print "Yes" if the string contains only digits, and "No" otherwise.


Constraints

1 <= len(S) <= 100


Example

Input

123456786543


Output

Yes


Explanation

Self Explanatory
'''

s = input()
print('Yes' if s.isdigit() else 'No')