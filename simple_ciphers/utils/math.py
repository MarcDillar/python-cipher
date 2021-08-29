"""
Math util functions

Functions:
    egcd
    modinv
    factors
"""

from random import randrange, getrandbits


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


def is_pseudo_prime(n, k=128):
    """
        Test if a number is pseudo prime
        using the Miller-Rabin method
    """

    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_number(length=1024):
    """
        Generate a prime number
        Parameters:
            length (int): length of the generated prime number in bits
    """

    while True:
        # generate random bits
        p = getrandbits(length)
        # apply a mask to set MSB and LSB to 1
        p |= (1 << length - 1) | 1

        if is_pseudo_prime(p):
            return p
