from authenticator import Authenticator

class Authorizor:
    permission_key = 1
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, permission_name):
        if permission_name not in self.permissions:
            self.permissions[self.permission_key] = permission_name
            self.permission_key += 1

authenticator = Authenticator()
authenticator.add_user('john', '12345')
authorizor = Authorizor(authenticator)
authorizor.add_permission("ajouter")
authorizor.add_permission("supprimer")
print(authorizor.permissions)