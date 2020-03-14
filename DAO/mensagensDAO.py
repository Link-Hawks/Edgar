
from connections.singletonConnection import SingletonConnection
from bson.objectid import ObjectId
import pymongo

class MensagensDAO:

    _mensagensCollection = SingletonConnection.get_collection('messages','messages')

    def buscar(self, usuario):
        usuario_id = usuario
        if usuario != 0:
            usuario_id = ObjectId(usuario)
        messages_by_user_query = {'$or': [{'to._id':usuario_id},{'from._id':usuario_id}]}
        print(messages_by_user_query)
        mensagens = self._mensagensCollection.find(messages_by_user_query).sort("time")
        return list(mensagens)

    def insert(self, mensagem):
        if mensagem["to"]["_id"] != 0:
            mensagem["to"]["_id"] = ObjectId(mensagem["to"]["_id"])
        if mensagem["from"]["_id"] != 0:
            mensagem["from"]["_id"] = ObjectId(mensagem["from"]["_id"])
        mensagem_retorno = self._mensagensCollection.insert_one(mensagem)
        mensagem["_id"] = mensagem_retorno.inserted_id
        return mensagem
 
    def ultimas_mensagens(self,usuario):
        print(usuario)
        messages_by_user_query = {'$or': [{'to._id':ObjectId(usuario["id"])},{'from._id':ObjectId(usuario["id"])}]}
        return list(self._mensagensCollection.find(messages_by_user_query).limit(30).sort("time",pymongo.DESCENDING))
         
