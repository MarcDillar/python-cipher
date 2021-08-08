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

    factors=[]

    for i in range(2, n + 1):
        if i > max:
            break
        if n % i == 0:
            factors.append(i)

    return factors
