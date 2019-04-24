class BotController:

    def __init__(self, bot):
        self.__bot = bot
        self.__resposta_valida = ""

    @staticmethod
    def __get_resposta_correta():
        print('Digite a resposta válida: ')
        resposta_correta = input('Resposta: ').capitalize()
        return resposta_correta

    def feedback_resposta(self, afirmacao_usuario):
        self.__resposta_valida = self.__bot.resposta_str

        if self.__bot.resposta.confidence < 0.7:
            print('A resposta do Edgar é válida? (S/N) ')
            valido = input('Resposta: ').upper()
            if 'N' in valido:
                self.corrigir(afirmacao_usuario)
            elif 'S' in valido:
                self.__bot.aprenda(self.__resposta_valida, afirmacao_usuario)

    def corrigir(self, afirmacao_usuario):
        self.__resposta_valida = BotController.__get_resposta_correta()
        self.__bot.aprenda(self.__resposta_valida, afirmacao_usuario)

    def responder(self):
        print(self.__bot.responda())

    def escutar(self, afirmacao_usuario):
        self.__bot.escute(afirmacao_usuario)

    def apresentar(self):
        print(self.__bot.apresentacao)
