from eliza.eliza import Eliza
from enum import Enum, auto
import xmpp
import time

# Dados do usuário de bot
USER_ID = 'android18@localhost'
PASSWORD = '123456'
RECEIVER = 'kuririn@localhost'

# Log de mensagens
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

INFO_TAG = f"{GREEN}[INFO]{RESET}"
MSG_TAG = f"{YELLOW}[MSG]{RESET}"
ERRO_TAG = f"{RED}[ERRO]{RESET}"

# Script do bot Eliza em https://github.com/jezhiggins/eliza.py
android18 = Eliza()

class LogType(Enum):
    MSG = auto()
    INFO = auto()
    ERRO = auto()


# Log de mensagens
def log(type: str, msg: str):
    if type == LogType.MSG:
        print(f"{MSG_TAG} | {msg}")
    elif type == LogType.INFO:
        print(f"{INFO_TAG} | {msg}")
    elif type == LogType.ERRO:
        print(f"{ERRO_TAG} | {msg}")

# Reponde as mensagens com o bot Eliza
def message_handler(conn, msg):

    if msg.getBody():
        log(LogType.MSG,"Mensagem recebida: " + msg.getBody())

        reply_text = android18.respond(msg.getBody())
        reply = xmpp.Message(RECEIVER, reply_text)
        reply.setAttr('type', 'chat')

        log(LogType.MSG,"Mensagem enviada: " + reply_text)
        conn.send(reply)


# Conecta ao servidor
def connect_server():
    log(LogType.INFO,"Conectando ao servidor XMPP...")

    jid = xmpp.protocol.JID(USER_ID)
    connection = xmpp.Client(jid.getDomain(), debug=False)

    if not connection.connect(server=(jid.getDomain(), 5222)):
        log(LogType.ERRO,"Não foi possível conectar.")
        raise IOError('Não foi possível conectar.')

    log(LogType.INFO,"Conexao estabelecida!")

    # Autenticar no servidor
    if not connection.auth(user=jid.getNode(), password= PASSWORD, resource=jid.getResource()):
        log(LogType.ERRO,"Não foi possível autenticar.")
        raise IOError('Não foi possível autenticar.')

    log(LogType.INFO,"Autenticação bem-sucedida!")

    return connection

client = connect_server()

client.RegisterHandler('message', message_handler)
client.sendInitPresence()

log(LogType.INFO,f"Bot {USER_ID} online")

# Loop de mensagens
try:
    while True:
        client.Process(1)
        time.sleep(1)
except KeyboardInterrupt:
    log(LogType.INFO,f"Bot {USER_ID} offline")
    client.disconnect()