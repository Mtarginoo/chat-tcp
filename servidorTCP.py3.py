# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets
from threading import Thread
import sys

clientesConectados = list();
socketList = list()

"""def inputMensagem(connectionSocket, addr, apelido):
    msg = ''
    while msg != 'sair()':
        try:
            connectionSocket.send(msg.encode('utf-8'))
        except:
            continue"""
        
def recvMensagem(connectionSocket, addr, apelido):
    global socketList
    recvmsgIN = ('%s entrou!' % (apelido))
    for i in socketList:
        if (i != connectionSocket):
            i.send(recvmsgIN.encode('utf-8'))
    recvmsg = ''
    while recvmsg != 'sair()':
        if recvmsg != '':
            recvmsg = ('%s diz: %s' % (apelido, recvmsg))
            print(recvmsg)
            for i in socketList:
                if (i != connectionSocket):
                    i.send(recvmsg.encode('utf-8'))
        try:
            recvmsg = connectionSocket.recv(1024)
            recvmsg = recvmsg.decode('utf-8')
        except:
            recvmsg = ''
    connectionSocket.send(recvmsg.encode('utf-8'))
    for i in socketList:
        if (i != connectionSocket):
            i.send(('%s saiu!' % (apelido)).encode('utf-8'))

def threadConnection(connectionSocket, addr):
    pedido = 'Digite o seu apelido: '
    pedido = pedido.encode('utf-8')
    connectionSocket.send(pedido)
    apelido = connectionSocket.recv(1024) # recebe o nickname do cliente
    apelido = apelido.decode('utf-8')
    # capitalizedSentence = sentence.upper() # converte em letras maiusculas
    print ('%s entrou!' % (apelido))
    global clientesConectados
    global socketList
    clientesConectados.append(apelido)
    socketList.append(connectionSocket)
    
    """t5 = Thread(target=inputMensagem, args=[connectionSocket, addr, apelido])
    t5.start()"""
    t3 = Thread(target=recvMensagem, args=[connectionSocket, addr, apelido])
    t3.start()
    # connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
    while t3.isAlive():
        continue
    for i in clientesConectados:
        if i == apelido:
            clientesConectados.remove(apelido)
            socketList.remove(connectionSocket)
    connectionSocket.close() # encerra o socket com o cliente 
    print('%s saiu!' %(apelido))

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 65000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
    
while 1:
    connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
    t1 = Thread(target=threadConnection, args=(connectionSocket, addr))
    t1.start()
    
    

serverSocket.close() # encerra o socket do servidor
