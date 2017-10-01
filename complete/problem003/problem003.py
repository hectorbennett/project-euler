"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

VAL = 600851475143


def prime_sieve(max_number):
    """Sieve of Eratosthenes"""
    prime_list = []

    is_prime = [True] * max_number
    is_prime[0] = is_prime[1] = False

    for i in range(max_number):
        if is_prime[i]:
            prime_list.append(i)
            for k in range(2 * i, max_number, i):
                is_prime[k] = False

    return prime_list


for j in reversed(prime_sieve(int(VAL ** 0.5))):
    if VAL % j == 0:
        print(j)
        break
