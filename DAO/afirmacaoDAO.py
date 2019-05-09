from pymongo import MongoClient


class AfirmacaoDAO:

    def __init__(self, afirmacao, id=None):
        self.afirmacao = afirmacao
        self.id = id

        if not id:
            statements = self._get_banco()
            statement = statements.find_one({"text": afirmacao})
            self.id = statement['_id']

    def alterar(self, nova_afirmacao):
        statements = self._get_banco()
        statements.update({"_id": self.id}, {"$set": {"text": nova_afirmacao}})

    def alterar_em_resposta_a(self, novo_em_resposta_a):
        statements = self._get_banco()
        statements.update({"_id": self.id}, {"$set": {"in_response_to": novo_em_resposta_a}})

    def adicionar_novo_campo(self, nome, valor):
        statements = self._get_banco()
        if nome in statements.find_one({'_id': self.id}).keys():
            raise Exception('já existe um campo com este nome.')
        else:
            statements.update({'_id': self.id}, {'$set': {nome: valor}})

    # Metodo a ser deletado após implementação da classe de conexão
    def _get_banco(self):
        cliente = MongoClient('127.0.0.1', 27017)
        db = cliente['chatterbot-database']
        statements = db.statements
        return statements
