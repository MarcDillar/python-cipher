"""
List util functions

Functions:
    most_frequent_elements
"""

def most_frequent_elements(l):
    result, max_count = [], 0
    for n in set(l):
        count = l.count(n)
        if count == max_count:
            result.append(n)
        elif count > max_count:
            result, max_count = [n], count
    return result