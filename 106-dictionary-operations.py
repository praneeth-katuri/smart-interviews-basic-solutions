'''
You are tasked with implementing a program that manipulates an empty Dictionary based on a series of commands.


Input Format

The first line of input contains an integer N, indicating the number of commands to follow. The next N lines contains any of the following commands:

insert K: Insert a key-value pair (K,1) into the Dictionary. If the key (K) already exists, increment the count associated with that key by 1.
search K: Search for a key (K) in the Dictionary. If the key exists, print True, otherwise print False.
delete K: Completely remove the key (K) from the Dictionary.
remove K: If the count associated with the key (K) is greater than 1, decrement the count by 1. If the count is 1, completely remove the key from the Dictionary.
get K: Retrieve the count associated with the key from the Dictionary.
size: Gives the size of the Dictionary.


Output Format

For size and search command, print the result. For the remaining commands, print the sorted (K:V) of the Dictionary separated by spaces (see example for more details). If the Dictionary is empty, skip printing the Dictionary.


Constraints

1 <= N <= 50

1 <= K <= 100

For delete K, remove K and get K commands => K ∈ {Keys in the Dictionary}


Example

Input

10
insert 5
insert 10
insert 66
insert 66
remove 66
search 10
delete 10
insert 3
get 3
size


Output

5:1 
5:1 10:1 
5:1 10:1 66:1 
5:1 10:1 66:2 
5:1 10:1 66:1 
True
5:1 66:1 
3:1 5:1 66:1 
1
3


Explanation

Self Explanatory
'''

d = {}
def print_dict(d):
    sort_d = sorted(d.items())
    print(' '.join(f"{k}:{v}" for k,v in sort_d))

n = int(input())
for _ in range(n):
    cmd = input().split()
    act = cmd[0]

    if act == 'insert':
        k = int(cmd[1])
        if k in d:
            d[k] += 1
        else:
            d[k] = 1
        print_dict(d)
    elif act == 'search':
        k = int(cmd[1])
        print('True' if k in d else 'False')
    elif act == 'delete':
        k = int(cmd[1])
        if k in d:
            del d[k]
        print_dict(d)
    elif act == 'remove':
        k = int(cmd[1])
        if k in d:
            if d[k] > 1:
                d[k] -= 1
            else:
                del d[k]
        print_dict(d)
    elif act == 'get':
        k = int(cmd[1])
        print(d.get(k, 0))
    elif act == 'size':
        print(len(d))
    elif act == 'size':
        print(len(d))