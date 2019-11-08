# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula
#

# importacao das bibliotecas
from socket import *
from threading import Thread
    
# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

def inputMensagem():
    msg = ''
    while msg != 'sair()':
        msg = input()
        clientSocket.send(msg.encode('utf-8'))
        
def recvMensagem():
    recvmsg = ''
    while recvmsg != 'sair()':
        if recvmsg != '':
            print(recvmsg)
        try:
            recvmsg = clientSocket.recv(1024)
            recvmsg = recvmsg.decode('utf-8')
        except:
            recvmsg = ''

pedido = clientSocket.recv(1024)
pedido = pedido.decode('utf-8')
print(pedido)
apelido = input()
clientSocket.send(apelido.encode('utf-8')) # envia o texto para o servidor

t1 = Thread(target=inputMensagem, args=())
t1.start()

t2 = Thread(target=recvMensagem, args=())
t2.start()

while t1.isAlive():
    continue

while t2.isAlive():
    continue

clientSocket.send(('%s saiu!' % apelido).encode('utf-8'))

# modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
# print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente