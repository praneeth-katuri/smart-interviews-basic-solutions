'''
You are given an integer N, denoting the number of people who need to be seated, and a list of M seats, where 0 represents a vacant seat and 1 represents an already occupied seat. Find whether all N people can find a seat, provided that no two people can sit next to each other.


Input Format
The first line of the input contains N denoting the number of people. The second line of input contains M denoting the number of seats. The third line of input contains the seats.


Output Format
If all N people can find seats, print YES otherwise NO.


Constraints

1 ≤ N ≤ 105

1 ≤ M ≤ 105

Ai ∈ {0, 1}


Example

Input

2

7

0 0 1 0 0 0 1


Output

YES


Explanation

The two people can sit at index 0 and 4.
'''

n = int(input())
m = int(input())
seats = list(map(int, input().split()))
seated = 0

i = 0
while i < m:
    if seats[i] == 0:
        if i == 0 or seats[i-1] == 0:
            if i == m-1 or seats[i+1] == 0:
                seated += 1
                seats[i] = 1
                i += 1
    i += 1

print("YES" if seated >= n else "NO")