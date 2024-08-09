'''
You are tasked with implementing a program that manipulates an empty list based on a series of commands.


Input Format

The first line of input contains an integer N, indicating the number of commands to follow. The next N lines contains any of the following commands:

1. append X: Appends the integer X to the end of the list.
2. count X: Count the number of occurrences of the integer X in the list.
3. reverse: Reverses the order of elements in the list.
4. insert Pos X: Inserts the integer X at the position Pos in the list.
5. sort: Sorts the elements of the list in ascending order.
6. index X: Gives the index of the first occurrence of the integer X in the list, or -1 if X is not found.
7. length: Gives the length of the list.
8. extend: Extends the list by appending it's current elements to itself.

Output Format

For count, index, and length command, print the result. For the remaining commands, print the updated list separated by spaces.


Constraints

1 <= N <= 50

1 <= X <= 100

0 <= Pos < length of the list


Example

Input

10

append 13

append 7

insert 1 6

extend

index 2

reverse

index 7

length

sort

count 6



Output

13

13 7

13 6 7

13 6 7 13 6 7

-1

7 6 13 7 6 13

0

6

6 6 7 7 13 13

2


Explanation

Self Explanatory
'''

lst = []
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "append":
        x = int(command[1])
        lst.append(x)
        print(*lst)
    elif command[0] == 'count':
        x = int(command[1])
        print(lst.count(x))
    elif command[0] == 'reverse':
        lst.reverse()
        print(*lst)
    elif command[0] == 'insert':
        pos = int(command[1])
        x = int(command[2])
        lst.insert(pos, x)
        print(*lst)
    elif command[0] == 'sort':
        lst.sort()
        print(*lst)
    elif command[0] == 'index':
        x = int(command[1])
        if x in lst:
            print(lst.index(x))
        else:
            print(-1)
    elif command[0] == "length":
        print(len(lst))
    elif command[0] == 'extend':
        lst.extend(lst)
        print(*lst)