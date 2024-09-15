'''
Given a string S of length N. You can apply the following operations any number of times:

1. In one operation you can remove any one occurrence of substring "AB" from S.
2. In one operation you can remove any one occurrence of substring "CD" from S.
Print the minimum possible length of the resulting string that you can obtain.

Note: The string concatenates after removing the substring and could produce new "AB" or "CD" substrings.


Input Format
The first and only line of input contains a string S.


Output Format
Print the minimum possible length of string S.


Constraints

'A' <= S[i] <= 'Z'

1 <= N <= 500


Example

Input

CCAAABBBDE


Output

2


Explanation

You can apply the following operations to the given string:

1st operation: Remove AB from the string, and the string becomes 'CCAABBDE.'
2nd operation: Remove AB from the string, and the string becomes 'CCABDE.'
3rd operation: Remove AB from the string, and the string becomes 'CCDE.'
4th operation: Remove CD from the string, and the string becomes 'CE.'

Furthermore, we cannot apply any more operations, and the minimum possible length is 2.
'''

s = input()
stack = []
for char in s:
    stack.append(char)

    if len(stack) >= 2:
        if (stack[-2] == 'A' and stack[-1] == 'B') or (stack[-2] == 'C' and stack[-1] == 'D'):
            stack.pop()
            stack.pop()
print(len(stack))