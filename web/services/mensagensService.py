from DAO.mensagensDAO import MensagensDAO
from services.edgarService import EdgarService
import json
import dateutil.parser
from datetime import datetime
class MensagensService:

    _botService = EdgarService()
    _dao = MensagensDAO()

    def buscar(self, usuario):
        mensagens = self._dao.buscar(usuario)
        return json.dumps (mensagens,indent=4, sort_keys=True, default=str,ensure_ascii = False)

    def responder(self, mensagem):
        print(mensagem)
        print("mensagem\n")
        mensagem['time'] = dateutil.parser.parse(mensagem['time'])
        self._dao.insert(mensagem)
        resposta = self._botService.responder(mensagem['message'])
        mensagem_bot = {
            "message": resposta["resposta"],
            "to": mensagem["from"],
            "from": mensagem["to"],
            "time": datetime.now()
        }
        mensagem_resposta = self._dao.insert(mensagem_bot)
        return json.dumps (mensagem_resposta, indent=4, sort_keys=True, default=str,ensure_ascii = False)

    def buscar_ultimas_mensagens(self, usuario):
        mensagens = self._dao.ultimas_mensagens(usuario)
        return json.dumps(mensagens,indent=4, sort_keys=True, default=str,ensure_ascii = False)

