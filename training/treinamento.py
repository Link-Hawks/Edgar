import sys
sys.path.append("..")

from models.edgar import Edgar
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class Treinamento:

    def __init__(self):
        self.__dados_treino = []
        self.__edgar = Edgar()
        self.__treinador = ListTrainer(self.__edgar.bot)
        self.__treinador_padrao = ChatterBotCorpusTrainer(self.__edgar.bot)

    def treinar(self, conversa):
        self.__treinador.train(conversa)

    def sobre_robo(self):
        self.treinar([
            'Qual é o seu nome?',
            'Meu nome é Edgar',
            'Quantos anos você tem?'
            f'Eu tenho {self.__edgar.idade} anos'
        ])

    def padrao_br(self):
        self.__treinador_padrao.train('chatterbot.corpus.portuguese')

    def saudacao(self):
        self.treinar([
            'Olá',
            'Oi, tudo bem?',
            'Tudo ótimo e com você?',
            'Eu vou bem',
            'Isso é ótimo de se ouvir',
            'Obrigado',
            'Não há de quê',
        ])
        self.treinar([
            'Oi',
            'Oi, tudo bem?',
            'Não estou muito bem',
            'É uma pena'
        ])
        self.treinar([
            'Eai',
            'Opa, eai tudo bom?',
            'Tudo ótimo e contigo?',
            'Eu estou ótimo'
        ])


edgar = Edgar()
if __name__ == '__main__' and not edgar.treinado:
    treinamento = Treinamento()
    treinamento.saudacao()
    treinamento.padrao_br()
    edgar.treinado = True

