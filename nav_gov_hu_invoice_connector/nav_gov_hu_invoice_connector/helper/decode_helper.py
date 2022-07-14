from Crypto.Cipher import AES


class DecodeHelper:
    @staticmethod
    def token(token, key):
        aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return aes.decrypt(token).decode('utf-8')
