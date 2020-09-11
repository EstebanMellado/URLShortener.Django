import random
import string

class shortener:
    token_size=6

    def __init__(self, token_size=None):
        self.token_size=token_size if token_size is not None else 6

    def issue_token(self):
        letters=string.ascii_letters
        return ''.join(random.choice(letters) for i in range(self.token_size))