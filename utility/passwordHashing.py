import hashlib
from config.configConstants import passwordSalt

class PasswordHashing:
    # hash the user password in sha256
    def getHashedPassword(self, password):
        salt = passwordSalt.SALT
        hashedPassword = hashlib.sha256(
            salt.encode() + password.encode()).hexdigest()
        return hashedPassword

    # match the user old password and new password
    def matchHashedPassword(self, oldPassword, newPassword):
        salt = passwordSalt.SALT
        hashedPassword = hashlib.sha256(
            salt.encode() + newPassword.encode()).hexdigest()  # convert the new password in sha256
        if oldPassword == hashedPassword:
            return True
        else:
            return False
