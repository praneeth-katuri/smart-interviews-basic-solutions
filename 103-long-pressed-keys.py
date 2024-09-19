'''
Observing your friend as they type their name on the keyboard, you notice that occasionally a key might be held down longer, causing a character to appear multiple times. After examining the sequence of typed characters, determine whether it's possible that the typed sequence corresponds to your friend's name. Print true if typed_name corresponds to your friend_name, otherwise print false.


Input Format

The first and only line of input contains two strings separated by space.


Output Format

Print true if typed_name corresponds to your friend_name, otherwise print false.


Constraints

1 ≤ len(friend_name), len(typed_name) ≤ 3000


Example

Input

raju rrraaajjjjjjjjjjjjjjuuuu


Output

true


Explanation

Self Explanatory
'''

name, typed = input().split()
def check(name, typed):
    i = j = 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j-1] == typed[j]:
            j += 1
        else:
            return False
    return i == len(name)

print('true' if check(name, typed) else 'false')