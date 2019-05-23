from pymongo import MongoClient
from os import system
from helpers.validacaohelper import ValidacaoHelper


class AfirmacaoDAO:

    def __init__(self, afirmacao, id=None):
        self.afirmacao = afirmacao
        self.id = id

        if not id:
            statements = self._get_banco()
            statement = statements.find_one({"text": afirmacao})
            self.id = statement['_id']

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

    def alterar(self, nova_afirmacao):
        statements = self._get_collection("statements")
        statements.update({"_id": self.id}, {"$set": {"text": nova_afirmacao}})
    
    def remover(self):
        self.statements.remove({'id': self.id})

    # Metodo a ser deletado após implementação da classe de conexão
    def _get_banco(self):
        if not ValidacaoHelper.rodando('mongo'):
            self._start_mongo_service()
        cliente = MongoClient('127.0.0.1', 27017)
        db = cliente['chatterbot-database']
        return db

    def _start_mongo_service(self):
        command_start_mongo_service = "systemctl start mongodb"
        senha_sudo = "senha123"
        system(f'echo "{senha_sudo}" | sudo -S {command_start_mongo_service}')

    def _get_collection(self, collection):
        db = self._get_banco()
        collection = db[collection]
        return collection
