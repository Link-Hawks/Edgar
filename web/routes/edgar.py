import sys
sys.path.append("..")

from web_main import app
from web_main import socketio
from flask import request, abort
from services.edgarService import EdgarService
from services.mensagensService import MensagensService
from flask_socketio import SocketIO, emit
from services.authService import AuthService
import json

_user = None

app.config['JSON_AS_ASCII'] = False


@socketio.on("connect")
def connectServer():
    print("Client connected")

@socketio.on('messages')
def get_messages(usuario):
    try:
        service = MensagensService()
        result = service.buscar_ultimas_mensagens(usuario)
        emit('mensagens', result)
    except Exception as ex:
        print(str(ex))

@app.route('/api/auth',methods=['POST'])
def autenticar():
    email = request.json['email']
    senha = request.json['password']
    service = AuthService()
    user = service.autenticar(email, senha)
    if user is not None:
        return user
    return abort(401)

@app.route('/api/edgar', methods=['POST'])
def conversar():
    if request.method == 'POST':
        afirmacao = ''
        try:
            afirmacao = request.json['afirmacao']
        except:
            return abort(400)
        service = EdgarService()
        resposta = service.responder_json(afirmacao)
        return resposta

@app.route('/api/edgar', methods=['PUT'])
def corrigir():
    if request.method == 'PUT':
        afirmacao_usuario = request.json['afirmacao_usuario']
        resposta_correcao = request.json['resposta_correcao']
        service = EdgarService()
        return service.corrigir(afirmacao_usuario, resposta_correcao)

@app.route('/api/mensagens', methods=['GET'])
def buscar_mensagens():
    usuario = int(request.args.get("user"))
    service = MensagensService()
    return service.buscar(usuario)

@app.route('/api/mensagens', methods=['POST'])
def responder_mensagens():
    print("enviando post")
    service = MensagensService()
    return service.responder(request.json)

