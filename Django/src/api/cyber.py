from hashlib import sha512
from .app_config import appConfig

class Cyber:
    # hashing the password
    @staticmethod
    def hash(plain_text):
        encoded_text = plain_text.encode("UTF-8") + appConfig.passwords_salt.encode("UTF-8")
        hashed_text = sha512(encoded_text).hexdigest()
        return hashed_text