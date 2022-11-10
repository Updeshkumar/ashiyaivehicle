
from config.configConstants import AESEncryptionKeys

# Encryption and Decryption 👌✔
class AESEncryption():
    def __init__(self):
        self.block_size = int(AESEncryptionKeys.AES_SIZE)
        
    def _pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)
    
    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

    def encrypt(self, plain_text):
        key = AESEncryptionKeys.AES_SECRET_KEY
        iv = AESEncryptionKeys.AES_SECRET_IVKEY
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        pad_plain_text = self._pad(plain_text)
        len_encrypted = encryptor.update(bytes(pad_plain_text, 'utf-8'))   
        return b64encode(len_encrypted).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        key = AESEncryptionKeys.AES_SECRET_KEY
        iv = AESEncryptionKeys.AES_SECRET_IVKEY
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        len_decrypted = decryptor.update(encrypted_text)
        return self.__unpad(len_decrypted).decode("utf-8")
    
    

    