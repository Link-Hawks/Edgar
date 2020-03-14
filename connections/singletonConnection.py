from os import system

from pymongo import MongoClient


class SingletonConnection(object):
    __cliente = None

    @classmethod
    def get_connection(cls):
        if cls.__cliente is None:
            cls.__cliente = MongoClient('127.0.0.1', 27017)
        return cls.__cliente

    @classmethod
    def get_banco(cls, nome_banco):
        db = cls.get_connection()[nome_banco]
        return db

    @classmethod
    def get_collection(cls, nome_collection, nome_banco):
        collection = cls.get_banco(nome_banco)[nome_collection]
        return collection

    @classmethod
    def _start_mongo_service(cls, senha_sudo):
        command_start_mongo_service = "systemctl start mongodb"
        senha_sudo = senha_sudo
        system(f'echo "{senha_sudo}" | sudo -S {command_start_mongo_service}')
