import logging
from os import system

from DAO.afirmacaoDAO import AfirmacaoDAO
from controllers.botController import BotController
from models.edgar import Edgar
from models.usuario import Usuario
from controllers.usuarioController import UsuarioController


def limpar_log():
    logger = logging.getLogger()
    logger.setLevel(logging.CRITICAL)
    system('clear')


afDAO = AfirmacaoDAO('Olá')
afDAO.adicionar_novo_campo('testando', 123)

edgar = Edgar()
bot_controller = BotController(edgar)
nome_usuario = UsuarioController.get_nome()
usuario = Usuario(nome_usuario)
usuario_controller = UsuarioController(usuario)

limpar_log()
bot_controller.apresentar()

while not usuario.quer_sair:
    usuario_controller.get_afirmacao()
    if not usuario.quer_sair:
        bot_controller.escutar(usuario.afirmacao)

        if usuario.quer_corrigir():
            bot_controller.corrigir(usuario.ultima_afirmacao)
        else:
            bot_controller.responder()
            bot_controller.feedback_resposta(usuario.afirmacao)
