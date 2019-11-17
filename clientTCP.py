"""
Universidade Federal do Rio Grande do Norte
Departamento de Engenharia de Computação e Automação
Disciplina: Redes de Computadores            Professor: Carlos Viegas
Autores: Matheus Targino Barbosa e Saul Pedro

"""
from socket import *
from threading import Thread
    
# definicao das variaveis
serverName = 'localhost'                                                                  # ip do servidor
serverPort = 65000                                                                        # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM)                                                # criacao do socket TCP
clientSocket.connect((serverName, serverPort))                                            # conecta o socket ao servidor

def inputMensagem():                                                       
    msg = ''
    while msg != 'sair()':
        msg = input()    
        newMsg = encodeProtocol(msg, apelido)
        clientSocket.send(newMsg.encode('utf-8'))
        clientSocket.send(''.encode('utf-8'))
        
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
    print("encerrando conexão com o servidor...")


def encodeProtocol(mensagem, apelido):
    aux = mensagem.split('(')
    if(aux[0] == 'privado'): 
        aux2 = aux[1]
        aux = aux2.split(')') 
        nicknamePrivado = aux[0]
        aux3 = mensagem.split(')')
        mensagem = aux3[1]
        nicknameMensagem = nicknamePrivado +'/*'+ mensagem #concatenando o nickname do destinatário da mensagem com a mensagem enviada em modo privado
        mensagem = nicknameMensagem
        comando = 'privado'
    elif(aux[0] == 'sair'):
        comando = 'sair'
        mensagem = ''
    elif(aux[0] == 'lista'):
        comando = 'lista'
        mensagem = ''    
    else:
        comando = ''
    sizeApelido = len(apelido)
    if(sizeApelido < 16):
        for i in range(16-sizeApelido):
            apelido = apelido + '*'    
    sizeComando = len(comando)
    if(sizeComando < 8):
        for i in range(8-sizeComando):
            comando = comando + '*'
    apelidoAux = apelido            
    comandoAux = comando
    tamanhoMsg = len(apelidoAux.encode()) + len(comandoAux.encode()) + len(mensagem) + 6
    tamanhoTanho = len(str(tamanhoMsg)) 
    novaMensagem = (str(tamanhoMsg + tamanhoTanho) + '/0' + apelido + '/0' + comando + '/0' + mensagem)
    return novaMensagem

pedido = clientSocket.recv(1024)
pedido = pedido.decode('utf-8')
print(pedido)
apelido = input()
apelidoBytes = apelido.encode()
while(len(apelidoBytes) > 16):
    print("O apelido deve conter no máximo 16 caracteres")
    print(pedido)
    apelido = input()
    apelidoBytes = apelido.encode()

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

clientSocket.close()                                          
