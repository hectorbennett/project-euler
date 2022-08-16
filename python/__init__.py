"""
Find prime numbers. Quite basic
"""

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

if __name__ == '__main__':
    for prime in prime_sieve(10):
        print(prime)