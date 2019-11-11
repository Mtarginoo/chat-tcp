from socket import *
from threading import Thread
import sys
    
# definicao das variaveis
serverName = 'localhost'                                                                  # ip do servidor
serverPort = 65000                                                                        # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM)                                                # criacao do socket TCP
clientSocket.connect((serverName, serverPort))                                            # conecta o socket ao servidor

finish = False

def inputMensagem():                                                       
    msg = ''
    global finish
    while msg != 'sair()':
        if(finish == True):
            break   
        msg = input()
        clientSocket.send(msg.encode('utf-8'))
            
        
def recvMensagem():                                                                           
    global finish
    recvmsg = ''                          
    while recvmsg != 'sair()':
        if recvmsg != '':
            print(recvmsg)
            print("oi")
        try:
            recvmsg = clientSocket.recv(1024)
            recvmsg = recvmsg.decode('utf-8')
        except:
            recvmsg = ''
    print("encerrando conexão com o servidor...")
    finish = True

              


pedido = clientSocket.recv(1024)
pedido = pedido.decode('utf-8')
print(pedido)
apelido = input()
clientSocket.send(apelido.encode('utf-8'))                                                # envia o texto para o servidor

t1 = Thread(target=inputMensagem, args=())                                                # instancia a thread de envio de mensagens
t1.start()                                                                                # incia a thread de envio de mensagens

t2 = Thread(target=recvMensagem, args=())                                                 # instancia a thread de recebimento de mensagens
t2.start()                                                                                # inicia a thread de recebimento de mensagens

while t1.isAlive():                                                                       # executa enquanto a thread de envio está ativa (msg != 'sair()')
        continue

while t2.isAlive():                                                                       # executa enquanto a thread de recebimento de mensagens está ativa (rcvmsg != 'sair())
        continue

clientSocket.send(('%s saiu!' % apelido).encode('utf-8'))                                 # envia para o servidor que o cliente saiu

clientSocket.close()                                                                      # encerramento o socket do cliente