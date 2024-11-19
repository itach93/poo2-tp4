import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.status = False

    def check_password(self, password) -> bool:
        encrypted_password = self._encrypt_password(password)
        return encrypted_password == self.password
    
    def _encrypt_password(self, password) -> str:
        '''
        Crypte le mot de passe en utilisant l'algorithme SHA-256
        '''
        password_encoded = password.encode('utf-8')
        return hashlib.sha256(password_encoded).hexdigest()