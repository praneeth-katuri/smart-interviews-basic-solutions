'''
Given a string, toggle the case of each character in the given string.

Input Format

The first and only input line contains a string S, consisting of lowercase and uppercase characters.

Output Format

Print the toggled string.


Constraints

1 <= len(S) <= 100


Example

Input

sMaRtInTeRvIeWs


Output

SmArTiNtErViEwS


Explanation

Self Explanatory
'''

text = input()
print(text.swapcase())