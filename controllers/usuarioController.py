class UsuarioController:

    def __init__(self, usuario):
        self.__usuario = usuario

    @staticmethod
    def get_nome():
        return input("Digite o seu nome: ")

    def get_afirmacao(self):
        nome_inicial_maiusculo = self.__usuario.nome.capitalize()
        self.__usuario.ultima_afirmacao = self.__usuario.afirmacao
        self.__usuario.afirmacao = input(f'{nome_inicial_maiusculo}: ').capitalize()
