# importacao das bibliotecas
from socket import * # sockets
import threading

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 65000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

def threadConnection(connectionSocket, addr):
    apelido = connectionSocket.recv(1024) # recebe o nickname do cliente / recv(1024) <- tamanho do buffer, deve ser potência de 2
    apelido = apelido.decode('utf-8')
    # capitalizedSentence = sentence.upper() # converte em letras maiusculas
    print ('%s entrou!' % (apelido))
    # connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
    connectionSocket.close() # encerra o socket com o cliente 
    
while 1:
    connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
    t1 = threading.Thread(target=threadConnection, args=(connectionSocket, addr))
    t1.start()
 