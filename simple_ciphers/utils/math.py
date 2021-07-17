"""
Math util functions

Functions:
    egcd
    modinv
"""


def egcd(a, b):
    '''
        Returns the result of the Extended Euclidian Algorithm

        Parameters:
            a, b (int, int): 2 integers

        Returns:
            g, x, y (int, int, int) : integers such that a*x + b*y = g = gcd(a, b)
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