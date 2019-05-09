from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ListTrainer


class Edgar:

    def __init__(self):
        self.__bot = ChatBot(
            name='Edgar',
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace'
            ],
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                }
            ],
            storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
            database_uri='mongodb://localhost:27017/chatterbot-database'
        )
        self.__resposta = None
        self.idade = 0
        self.treinado = False

    @property
    def bot(self):
        return self.__bot

    @property
    def resposta(self):
        return self.__resposta

    @property
    def resposta_str(self):
        return f'{self.__resposta}'

    def responda(self):
        if self.__resposta:
            return f"Edgar: {self.__resposta}. Confiança {self.__resposta.confidence}. "
        else:
            return "Não há afirmações a serem respondidas."

    def escute(self, sentenca):
        self.__resposta = self.__bot.generate_response(Statement(sentenca))

    def aprenda(self, resposta_valida, sentenca):
        self.__resposta = resposta_valida
        treinador_resposta_correta = ListTrainer(self.__bot)
        treinador_resposta_correta.train([sentenca, resposta_valida])

    @property
    def apresentacao(self):
        return f'\t\t {"*" * 15} Programa de testes com o robô Edgar {"*" * 15} ' \
            '\nVocê terá uma conversa com o Edgar, para sair digite "Edgar, por hoje é só"'
