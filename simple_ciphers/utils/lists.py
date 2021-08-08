"""
List util functions

Functions:
    most_common
"""

from collections import Counter


def most_common(my_list, n=1):
    c = Counter(my_list)
    return [x[0] for x in c.most_common(n)]
