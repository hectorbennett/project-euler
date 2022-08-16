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


def highest_common_factor(a, b):
	if b == 0:
		return a
	else:
		return highest_common_factor(b, a % b)

def lowest_common_multiple(a,b):
	return abs(a * b) // highest_common_factor(a,b) 


def prime_factors(n):
    return [p for p in prime_sieve(n+1) if n % p == 0]

def largest_prime_factor(n):
    return max(prime_factors(n))

def coprime(a, b):
    """
    Two numbers are coprime if their highest common factor is 1.
    """
    return highest_common_factor(a, b) == 1


def multiplicative_order(a, n):
    """
    In number theory, given a positive integer n and an integer a
    coprime to n, the multiplicative order of a modulo n is the
    smallest positive integer k such that a^k ≡ 1 (mod n)

    https://en.wikipedia.org/wiki/Multiplicative_order
    """
    if not coprime(a, n):
        return 0
    k = 1
    while a**k % n > 1:
        k += 1
    return k
