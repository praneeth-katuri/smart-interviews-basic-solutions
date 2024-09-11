'''
Given a string, print the count of vowels and consonants in the string.


Input Format
Input contains a string S, consisting of lowercase and uppercase characters.


Output Format
Print the count of vowels and consonants in the given string, separated by space.


Constraints
1 <= len(S) <= 100


Example

Input
abxbbiAaspw


Output
4 7


Explanation

Self Explanatory
'''

s = input().lower()
vowels = ["a", "e", "i", "o", "u"]
vowels_count = 0
cons_count = 0
for char in s:
    if char in vowels:
        vowels_count += 1
    else:
        cons_count += 1

print(vowels_count, cons_count)