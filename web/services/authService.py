import json
from connections.singletonConnection import SingletonConnection
import hashlib 
SECRET_KEY = 'REVEX'


class AuthService:

    def _autenticar(self, email, senha):
        users = SingletonConnection.get_collection("users", "messages")
        print(hashlib.md5(f"{SECRET_KEY}link20256800{SECRET_KEY}".encode()).hexdigest())
        user = users.find_one({"email": email, "authToken":hashlib.md5(f"{SECRET_KEY}{senha}{SECRET_KEY}".encode()).hexdigest()})
        return user
        

    def autenticar(self, email, senha):
        user = self._autenticar(email,senha)
        if user is None:
            return None
        return json.dumps(user, indent=4, sort_keys=True, default=str,ensure_ascii = False)