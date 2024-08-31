'''
Given an integer N. Print the count of permutations for the numbers from 1 to N, considering that prime numbers should be placed at positions with prime indices (1 - based indexing). As the result might be a large number, print the output % 1e9 + 7.


Input Format

The first and only line of input contains an integer N.


Output Format

Print the count of permutations.


Constraints

1 ≤ N ≤ 100


Example

Input

8


Output

576


Explanation

Self Explanatory
'''

n = int(input())
mod = 10**9 + 7

is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False

prime_count = sum(is_prime[1:n+1])
non_prime_count = n - prime_count

prime_permutations = 1
for i in range(2, prime_count + 1):
    prime_permutations = (prime_permutations * i) % mod

non_prime_permutations = 1
for i in range(2, non_prime_count+1):
    non_prime_permutations = (non_prime_permutations * i) % mod

total = (prime_permutations * non_prime_permutations) % mod
print(total)