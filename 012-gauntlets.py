'''
You have a collection of N gauntlets, each with a specific color represented by A[i]. Your goal is to maximize the number of pairs by repeatedly pairing up gauntlets of the same color. Determine the maximum number of pairs that can be formed.


Input Format

The first line of input contains an integer N. The second line of input contains an array of size N.


Output Format

For the given input, print a single line representing the answer.


Constraints

1 ≤ N ≤ 102

1 ≤ Ai ≤ 103


Example

Input

6

4 1 7 4 1 4


Output

2

Explanation

You can do the operation twice as follows.

--> Choose two gauntlets with the color 1 and pair them.
--> Choose two gauntlets with the color 4 and pair them.

Then, you will be left with one sock with the color 4 and another with the color 7, so you can no longer do the operation. There is no way to do the operation three or more times, so you should print 2.
'''

n = int(input())
a = list(map(int, input().split()))

freq = {}
for color in a:
    freq[color] = freq.get(color, 0) + 1

total_pairs = 0
for count in freq.values():
    total_pairs += count // 2

print(total_pairs)