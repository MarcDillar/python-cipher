import string
from langid.langid import LanguageIdentifier, model


class Hacker:
    def __init__(self, language="en"):
        '''
        Create a AffineCipherHacker instance

        Parameters:
            language (str, optionnal):
                Language code (ISO 639-1) used by the message
                that needs to be decrypted.
                'en' by default.
        '''

        self.symbols_sets = [
            string.printable,
            string.ascii_letters,
            string.ascii_lowercase,
            string.ascii_uppercase,
            string.ascii_letters + string.whitespace,
            string.ascii_lowercase + string.whitespace,
            string.ascii_uppercase + string.whitespace
        ]
        self.language = language
        self.lang_identifier = LanguageIdentifier.from_modelstring(
            model,
            norm_probs=True
        )

    def _candidate(self, message, p):
        lang, prob = self.lang_identifier.classify(message)
        if lang == self.language and prob >= p:
            return True, {
                "text": message,
                "p": prob
            }
        return False, None

    def _get_candidate(self, cipher, p, **kwargs):
        decrypted_message = cipher.decrypt(**kwargs)

        is_candidate, candidate = self._candidate(decrypted_message, p)

        if is_candidate:
            return candidate

    @staticmethod
    def _clean_list(decrypted_messages):
        decrypted_messages = sorted(
            decrypted_messages,
            key=lambda x: x["p"],
            reverse=True
        )

        final_list = []
        for message in decrypted_messages:
            text = message["text"]
            if text not in final_list:
                final_list.append(text)

        return final_list