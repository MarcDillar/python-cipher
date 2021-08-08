import re


def remove_non_letters(s):
    return re.compile('[^a-zA-Z]').sub('', s)
