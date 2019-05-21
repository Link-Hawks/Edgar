from subprocess import check_output
from shlex import quote

from pygame import mixer, time, event
from pygame.mixer import init


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
            #self.responder(f"A confiança da resposta é de: {confianca_resposta} porcento")
           # print('A resposta do Edgar é válida? (S/N) ')
           # valido = input('Resposta: ').upper()
          #  if 'N' in valido:
           #     self.corrigir(afirmacao_usuario)
           # elif 'S' in valido:
           #     self.__bot.aprenda(self.__resposta_valida, afirmacao_usuario)

    def corrigir(self, afirmacao_usuario):
        self.__resposta_valida = BotController.__get_resposta_correta()
        self.__bot.aprenda(self.__resposta_valida, afirmacao_usuario)

    def responder(self, afirmacao=''):
        afirmacao = self.__bot.responda() if not afirmacao else afirmacao

        # Finally não funciona.
        try:
            self.responder_por_voz(afirmacao, True)
            self.responder_por_texto(afirmacao, True)
        except:
            self.responder_por_texto(afirmacao,True)

    def responder_por_voz(self, afirmacao, troll_mode=False):
        if troll_mode:
            from requests import get
            som_troll = f'https://www.myinstants.com/media/sounds/{self.__bot.sentenca_usuario.lower()}.mp3'
            r = get(som_troll)
            path = f'/home/renan/Documents/projetos/Edgar/Sounds/{self.__bot.sentenca_usuario}.mp3'

            with open(path, 'wb') as f:
                f.write(r.content)

            music_path = f"Sounds/{self.__bot.sentenca_usuario}.mp3"
            init()
            try:
                mixer.music.load(music_path)
            except Exception as e:
                print('erro ao carregar som '+ str(e))
            mixer.music.play()
            mixer.music.set_volume(1)

            clock = time.Clock()
            clock.tick(10)

            while mixer.music.get_busy():
                event.poll()
                clock.tick(10)

        idioma = "pt"
        limpar_log = "&> /dev/null"
        resposta_edgar = afirmacao
        resposta_segura = quote(resposta_edgar)
        executar_espeak = f"espeak -v{idioma} {resposta_segura} {limpar_log}"
        check_output(executar_espeak, shell=True)

    def responder_por_texto(self, afirmacao,troll_mode=False):
        if not troll_mode:
            resposta_edgar = afirmacao
            print(f"Edgar: {resposta_edgar}")

    def escutar(self, afirmacao_usuario):
        self.__bot.escute(afirmacao_usuario)
        if 'cante' in afirmacao_usuario:
            self.__bot.cantar()

    def apresentar(self):
        print(self.__bot.apresentacao)
