import hashlib


class PasswordHash:
    @staticmethod
    def create(password):
        return hashlib.sha512(password.encode("utf-8")).hexdigest().upper()
