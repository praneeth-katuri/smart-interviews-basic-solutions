'''
Given a string, compress the given string. See the example for more details.


Input Format

Input contains a string S, consisting of lowercase and uppercase characters.


Output Format

Print the compressed string.


Constraints

1 <= len(S) <= 100


Example

Input

aaabbbbhhheaaAsssssss


Output

a3b4h3e1a2A1s7


Explanation

In the given string, a is repeating for 3 times - after compression a3.

Similarly,

b is repeating for 4 times - b4

h is repeating for 3 times - h3

e is repeating for 1 time - e1

a is repeating for 2 times - a2

A is repeating for 1 time - A1

s is repeating 7 times - s7
'''

count  = 1
s = input()

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        print(f"{s[i-1]}{count}", end = "")
        count = 1
print(f"{s[len(s)-1]}{count}", end = "")