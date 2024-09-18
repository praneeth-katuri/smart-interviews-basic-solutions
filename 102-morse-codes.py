'''
Given an array of strings A, where each string can be formed by combining the Morse code representation of individual letters.

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

The full table for the 26 letters of the English alphabet is given above. For example, "abc" can be written as ".--...-.-.", which is the concatenation of ".-", "-...", and "-.-.". We will call such a concatenation the transformation of a word. Print the number of different transformations among all A we have.


Input Format

First line of input contains the size of the array N. The second line of input contains array of strings separated by spaces.


Output Format

Print the number of different transformations among all A we have.


Constraints

1 ≤ A.length ≤ 100

1 ≤ A[i].length ≤ 12

A[i] consists of lowercase English letters.


Example

Input

4

abc bze abnn xyz


Output

3


Explanation

"abc" -> ".--...-.-."

"bze" -> "-...--..."

"adek" -> ".--...-.-."

"xyz" -> "-..--.----.."


There are 3 different transformations: ".--...-.-." , "-...--..." and "-..--.----..".
'''

morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
n = int(input())
A = list(map(str, input().split()))

uniq = set()

for word in A:
    morse = ''.join(morse_code[ord(char) - ord('a')] for char in word)
    uniq.add(morse)

print(len(uniq))