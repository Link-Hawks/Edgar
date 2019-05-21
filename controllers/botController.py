from subprocess import check_output
from shlex import quote

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
            confianca_resposta = int(self.__bot.resposta.confidence) * 100
            self.responder(f"A confiança da resposta é de: {confianca_resposta} porcento")
            print('A resposta do Edgar é válida? (S/N) ')
            valido = input('Resposta: ').upper()
            if 'N' in valido:
                self.corrigir(afirmacao_usuario)
            elif 'S' in valido:
                self.__bot.aprenda(self.__resposta_valida, afirmacao_usuario)

    def corrigir(self, afirmacao_usuario):
        self.__resposta_valida = BotController.__get_resposta_correta()
        self.__bot.aprenda(self.__resposta_valida, afirmacao_usuario)

    def responder(self, afirmacao=''):
        afirmacao = self.__bot.responda() if not afirmacao else afirmacao

        # Finally não funciona.
        try:
            self.responder_por_voz(afirmacao)
            self.responder_por_texto(afirmacao)
        except:
            self.responder_por_texto(afirmacao)

    def responder_por_voz(self, afirmacao):
        idioma = "pt"
        limpar_log = "&> /dev/null"
        resposta_edgar = afirmacao
        resposta_segura = quote(resposta_edgar)
        executar_espeak = f"espeak -v{idioma} {resposta_segura} {limpar_log}"
        check_output(executar_espeak, shell=True)

    def responder_por_texto(self, afirmacao):
        resposta_edgar = afirmacao
        print(f"Edgar: {resposta_edgar}")

    def escutar(self, afirmacao_usuario):
        self.__bot.escute(afirmacao_usuario)
        if 'cante' in afirmacao_usuario:
            self.__bot.cantar()

    def apresentar(self):
        print(self.__bot.apresentacao)
