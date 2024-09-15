'''
Find the minimum number of characters to add to a password (P) to ensure that P meets the following criteria:

1. Contains at least 6 characters.
2. Contains at least one digit.
3. Contains at least one lowercase character.
4. Contains at least one uppercase character.
5. Contains at least one special character (!@#$%^&*()-+).


Input Format

First and only line of input contains a string P.


Output Format

Print the minimum number of characters that has to be added to P.


Constraints

1 <= len(P) <=50

P[i] ∈ {[a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ]}.


Example

Input

He!!0


Output

1


Explanation

The given password P already contains one digit, one lowercase character, one uppercase character and one special character. However, it should also contain at least 6 characters. So we need to add 1 character to ensure it meets all the criteria.
'''

def strong_password(P):
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False

    special_chars = {'!', '@', '$', '%', '^', '&', '*', '(', ')', '-', '+'}

    for char in P:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char in special_chars:
            has_special = True
    
    missing_chars = 0
    if not has_digit:
        missing_chars += 1
    if not has_lower:
        missing_chars += 1
    if not has_upper:
        missing_chars += 1
    if not has_special:
        missing_chars += 1

    missing_length = max(0, 6-len(P))
    return max(missing_chars, missing_length)

P = input()
print(strong_password(P))