'''
Given a string, reverse the given string in place and then print it.


Note:

Do not use any inbuilt functions / libraries for your main logic.


Input Format
The input contains a string S, consisting of ASCII characters.


Output Format

Print the reversed string.


Constraints

1 <= len(s) <= 100


Example

Input

smart


Output

trams


Explanation

Self Explanatory
'''

term = input()
reversed_text = ''
for char in term: 
    reversed_text = char + reversed_text

print(reversed_text)