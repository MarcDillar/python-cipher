"""
Math util functions

Functions:
    egcd
    modinv
    factors
"""


def egcd(a, b):
    '''
        Returns the result of the Extended Euclidian Algorithm

        Parameters:
            a, b (int, int): 2 integers

        Returns:
            g, x, y (int, int, int) :
            integers such that a*x + b*y = g = gcd(a, b)
    '''

    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    '''
        Returns the Modular Inverse of 2 integers

        Parameters:
            a, m (int, int): 2 integers

        Returns:
           int : modular inverse
    '''
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def factors(n, max=None):
    '''
        Returns the factors of n
        that are grater than 1 and lower than max

        Parameters:
            n (int)
            max (int, optionnal):
                equal to n by default

        Returns:
           list(int) : list of factors
    '''

    if not max:
        max = n

    factors = []

    for i in range(2, n + 1):
        if i > max:
            break
        if n % i == 0:
            factors.append(i)

    return factors


def prime_eratosthenes(n):
    """Return all prime numbers below an upperbound

    Parameters:
        n (int): upper bound

    Returns:
        prime_list: list of prime numbers lower than n
    """
    prime_list = []
    for i in range(2, n+1):
        if i not in prime_list:
            for j in range(i*i, n+1, i):
                prime_list.append(j)
    return prime_list


def is_prime(n):
    """
    Return True if the integer parameter is prime
    """
    if (n < 2 or (n > 2 and n % 2 == 0) or (n > 3 and n % 3 == 0)):
        return False
    if n < 9:
        return True

    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0 or n % (f+2) == 0:
            return False
        f += 6
    return True
