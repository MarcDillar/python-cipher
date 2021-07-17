import string
from langid.langid import LanguageIdentifier, model

class Hacker:
    def __init__(self, language="en"):
        '''
        Create a AffineCipherHacker instance

        Parameters:
            language (str, optionnal):
                Language code (ISO 639-1) used by the message that needs to be decrypted.
                'en' by default.
        '''

        self.symbols_sets=[
            string.printable,
            string.ascii_letters,
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.ascii_letters + string.whitespace,
            string.ascii_lowercase + string.whitespace,
            string.ascii_uppercase + string.whitespace
        ]
        self.language = language
        self.lang_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)