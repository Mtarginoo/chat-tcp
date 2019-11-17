"""
Universidade Federal do Rio Grande do Norte
Departamento de Engenharia de Computação e Automação
Disciplina: Redes de Computadores            Professor: Carlos Viegas
Autores: Matheus Targino Barbosa e Saul Pedro

"""


from socket import * # sockets
from threading import Thread

clientesConectados = list()
socketList = list()

        
def recvMensagem(connectionSocket, addr, apelido):
    global socketList
    recvmsgIN = ('%s entrou!' % (apelido))
    for i in socketList:
        if (i != connectionSocket):
            i.send(recvmsgIN.encode('utf-8'))
    mensagem = ''
    comando = ''
    while comando != 'sair':
        if comando == 'privado':
            y = mensagem.split('/*')
            destino = y[0]
            mensagem = ('%s enviou em privado: '% (apelido) + y[1])
            cont = 0
            for nome in clientesConectados:
                if nome == destino:
                    socketList[cont].send(mensagem.encode('utf-8'))
                    break
                else:
                    cont = cont + 1
            comando = ''
            mensagem = ''
        elif comando == 'lista':
            enviarLista(connectionSocket)
            comando = ''
            mensagem = ''
        else:
            if mensagem != '':
                mensagem = ('%s diz: %s' % (apelido, mensagem))
                print(mensagem)
                for i in socketList:
                    if (i != connectionSocket):
                        i.send(mensagem.encode('utf-8'))
            try:
                recvmsg = connectionSocket.recv(1024)
                recvmsg = recvmsg.decode('utf-8')
                tamanho, nick, comando, mensagem = decodeProtocol(recvmsg)
            except:
                mensagem = ''
    comando = 'sair()'            
    connectionSocket.send(comando.encode('utf-8'))
    for i in socketList:
        if (i != connectionSocket):
            i.send(('%s saiu!' % (apelido)).encode('utf-8'))


def comandList():                                                             # recebe o comando de envio da lista
    comand = ''
    while 1:
        comand = input()
        if comand == 'lista()':
            print("Lista dos clientes conectados ao servidor:")   
            imprimirLista()
            
                
def imprimirLista():                                                          # imprime a lista de clientes conectados
    global clientesConectados
    global socketList
    for i in range(len(clientesConectados)):
        convstr = str(socketList[i])
        spt = convstr.split("raddr=(")
        convstr = str(spt[1])
        spt2 = convstr.split(")")
        ipPort = spt2[0]
        ipPortNick = "<" + ipPort + ", " + clientesConectados[i] + ">"
        print(ipPortNick)
        
def enviarLista(connectionSocket):                                            # envia a lista de clientes conectados para o cliente
    global clientesConectados
    global socketList
    for i in range(len(clientesConectados)):
        convstr = str(socketList[i])
        spt = convstr.split("raddr=(")
        convstr = str(spt[1])
        spt2 = convstr.split(")")
        ipPort = spt2[0]
        ipPortNick = "<" + ipPort + ", " + clientesConectados[i] + ">"
        connectionSocket.send(ipPortNick.encode('utf-8'))

def decodeProtocol(msgRecebida):                                               # decodifica a mensagem recebida do cliente
    header = msgRecebida.split('/0')                                         
    size = header[0]
    nick = header[1]
    cmd = header[2]
    data = header[3]
    nickAux = nick.split('*')
    nick = nickAux[0]
    cmdAux = cmd.split('*')
    cmd = cmdAux[0]
    return size, nick, cmd, data
    

def threadConnection(connectionSocket, addr):
    pedido = 'Digite o seu apelido (O apelido não pode conter o caractere "*"):'
    pedido = pedido.encode('utf-8') 
    connectionSocket.send(pedido)                                               # envia para os clientes a requisitação do pedido do apelido
    apelido = connectionSocket.recv(1024)                                       # recebe o nickname do cliente
    apelido = apelido.decode('utf-8') 
    print ('%s entrou!' % (apelido))                                            # mostra no servidor que um cliente se conectou
    global clientesConectados                                                   # lista com o nickname dos clientes conectados
    global socketList                                                           # lista com os sockets dos clientes
    clientesConectados.append(apelido)                                          # adiciona na lista os nicknames dos clientes conectados
    socketList.append(connectionSocket)                                         # adiciona na lista o socket dos clientes conectados
    
    t3 = Thread(target=recvMensagem, args=[connectionSocket, addr, apelido]) 
    t3.start()                                                                  # inicialização do socketo redecibmento de mensagensd
                                             
    while t3.isAlive():                                                         # executa enquanto a thread t3 estiver ativa (input != sair())
        continue

    for i in clientesConectados: 
        if i == apelido:
            clientesConectados.remove(apelido)
            socketList.remove(connectionSocket)
    connectionSocket.close()                                                    # encerra o socket com o cliente 
    print('%s saiu!' %(apelido))


# definicao das variaveis

serverName = ''                                                                # ip do servidor (em branco)
serverPort = 65000                                                             # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM)                                     # criacao do socket TCP
serverSocket.bind((serverName,serverPort))                                     # bind do ip do servidor com a porta
serverSocket.listen(1)                                                         # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

t4 = Thread(target=comandList, args =())                                       # instancia a thread para listar usuários no terminal do servidor
t4.start()                                                                     #inicia a thread de listagem de usuários no terminal do servidor
 
while 1:
    connectionSocket, addr = serverSocket.accept()                             # aceita as conexoes dos clientes
    t1 = Thread(target=threadConnection, args=(connectionSocket, addr))        # instancia a thread de conexão
    t1.start()                                                                 # inicia a thread de conexão
                                                            
                                                                
serverSocket.close()                                          
