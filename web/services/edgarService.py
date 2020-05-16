from models.edgar import Edgar
from datetime import datetime
from DAO.mensagensDAO import MensagensDAO
import json

class EdgarService:

    def responder(self, afirmacao_usuario):
        edgar = Edgar()
        edgar.escute(afirmacao_usuario)
        resposta_edgar = edgar.responda()
        resposta = {
            'resposta': resposta_edgar,
            'afirmação': afirmacao_usuario,
            'confianca': edgar.resposta.confidence,
            'hora': datetime.utcnow()
        }
        return resposta

    def responder_json(self, afirmacao_usuario):
        resposta  = self.responder(afirmacao_usuario)
        
        if float(resposta["confianca"]) < 0.7:
            resposta["resposta"] = "Eu não sei responder a isto"

        str_resposta = json.dumps(resposta,indent=4, sort_keys=True, default=str,ensure_ascii = False)
        return str_resposta

    def corrigir(self, afirmacao_usuario, resposta_valida):
        edgar = Edgar()
        edgar.aprenda(resposta_valida, afirmacao_usuario)

    def aprender(self,  afirmacao_usuario, resposta_valida):
        self.corrigir(afirmacao_usuario, resposta_valida)
        return json.dumps ({
            'resposta': resposta_valida,
            'afirmação': afirmacao_usuario,
            'confiança': 1.0,
            'hora': datetime.utcnow()
        },indent=4, sort_keys=True, default=str,ensure_ascii = False)

