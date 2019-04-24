class Usuario:

    def __init__(self, nome):
        self.nome = nome
        self.afirmacao = ""
        self.quer_sair = False
        self.ultima_afirmacao = ""

    def quer_sair(self):
        return self.afirmacao.lower().find('por hoje é só') != -1

    def quer_corrigir(self):
        return self.afirmacao.lower().find('quero corrigir') != -1
 
