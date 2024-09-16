'''
Given two strings A and B consisting of lowercase characters, check if they are anagrams. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutations of string A must be the same as string B.


Input Format

The first line of input contains string A. The second line of input contains string B.


Output Format

Print "TRUE" if A and B are anagrams otherwise "FALSE".


Constraints

1 ≤ len(A), len(B) ≤ 104


Example

Input

smartinterviews

viewsintersmart


Output

TRUE


Explanation

Self Explanatory
'''

def check_anagram(a, b):
    if len(a) != len(b):
        return False
    
    freq_a = {}
    freq_b = {}

    for char in a:
        if char in freq_a:
            freq_a[char] += 1
        else:
            freq_a[char] = 1

    for char in b:
        if char in freq_b:
            freq_b[char] += 1
        else:
            freq_b[char] = 1

    return freq_a == freq_b

a = input().strip()
b = input().strip()
if check_anagram(a,b):
    print("TRUE")
else:
    print("FALSE")