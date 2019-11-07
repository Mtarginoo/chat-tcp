# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 65000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

apelido = input('Digite o seu apelido: ')
clientSocket.send(apelido.encode('utf-8')) # envia o texto para o servidor
# modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
# print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente

