'''
Given a string, you have to check whether it is a square string. A string is said to be square if it is some string written twice in a row. For example, the strings "cc", "zazazaza", and "papa" are square. But "abc", and "abaaaabb" are not square.


Input Format

Input contains a string S.


Output Format

Print "Yes" if the string S is square. Otherwise print "No".


Constraints

1 <= |S| <= 103

'a' <= S[i] <= 'z'


Example

Input

aabaabaabaab


Output

Yes


Explanation

The given string can be formed by adding the string "aabaab" 2 times.
'''

def check_square_string(string):
    if len(string) % 2 == 0:
        mid = len(string) // 2
        first_half = string[:mid]
        second_half = string[mid:]

        if first_half == second_half:
            return "Yes"
    return "No"

string = input()
print(check_square_string(string))