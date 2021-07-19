"""Simple Dictionary Class

Classes:
    Dictionary
"""

import os


class Dictionary:
    '''
    Simple Dictionary Class

    ...

    Attributes
    ----------
    words : list
        List of words in the dictionary passed as argument

    '''

    def __init__(self, lang="en"):
        '''
        Create a Dictionary instance.

        Parameters:
            lang (str, optionnal):
                2-letter language code. "en" by default.
                The list of words is read from the corresponding
                file in the "words_list" folder.
        '''
        self.lang = lang.lower()

        directory = os.path.dirname(__file__)
        path = f"words_list/{self.lang}.txt"
        fo = open(os.path.join(directory, path))
        self.words = fo.read().split('\n')
        fo.close()
