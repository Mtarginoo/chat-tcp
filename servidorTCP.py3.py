<<<<<<< HEAD
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

"""def inputMensagem():
    msg = ''
    while msg != 'sair()':
        connectionSocket.send(msg.encode('utf-8'))"""
        
def recvMensagem(connectionSocket, addr, apelido):
    recvmsg = ''
    while recvmsg != 'sair()':
        if recvmsg != '':
            print('%s diz: %s' % (apelido, recvmsg))
        try:
            recvmsg = connectionSocket.recv(1024)
            recvmsg = recvmsg.decode('utf-8')
        except:
            recvmsg = ''
    connectionSocket.send(recvmsg.encode('utf-8'))

def threadConnection(connectionSocket, addr):
    pedido = 'Digite o seu apelido: '
    pedido = pedido.encode('utf-8')
    connectionSocket.send(pedido)
    apelido = connectionSocket.recv(1024) # recebe o nickname do cliente
    apelido = apelido.decode('utf-8')
    # capitalizedSentence = sentence.upper() # converte em letras maiusculas
    print ('%s entrou!' % (apelido))
    """t2 = Thread(target=inputMensagem, args=())
    t2.start()"""
    t3 = Thread(target=recvMensagem, args=[connectionSocket, addr, apelido])
    t3.start()
    # connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
    while t3.isAlive():
        continue
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
=======
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

"""def inputMensagem():
    msg = ''
    while msg != 'sair()':
        connectionSocket.send(msg.encode('utf-8'))"""
        
def recvMensagem(connectionSocket, addr, apelido):
    recvmsg = ''
    while recvmsg != 'sair()':
        if recvmsg != '':
            print('%s diz: %s' % (apelido, recvmsg))
        try:
            recvmsg = connectionSocket.recv(1024)
            recvmsg = recvmsg.decode('utf-8')
        except:
            recvmsg = ''
    connectionSocket.send(recvmsg.encode('utf-8'))

def threadConnection(connectionSocket, addr):
    pedido = 'Digite o seu apelido: '
    pedido = pedido.encode('utf-8')
    connectionSocket.send(pedido)
    apelido = connectionSocket.recv(1024) # recebe o nickname do cliente
    apelido = apelido.decode('utf-8')
    # capitalizedSentence = sentence.upper() # converte em letras maiusculas
    print ('%s entrou!' % (apelido))
    """t2 = Thread(target=inputMensagem, args=())
    t2.start()"""
    t3 = Thread(target=recvMensagem, args=[connectionSocket, addr, apelido])
    t3.start()
    # connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
    while t3.isAlive():
        continue
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
>>>>>>> bccd8aeaa282d06f193f4b0a4b2a7932a3d03b15
