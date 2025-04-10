# â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—  â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—
# â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—
# â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘
# â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘
# â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘
# â•šâ•â•â•â•â•â•  â•šâ•â•â•â•â•â•â•šâ•â•  â•šâ•â• UFRN 2024
#
# PROF CARLOS M D VIEGAS (C)
# carlos.viegas '@' ufrn.br
#
# ----------------------------------------------- 
#
# SCRIPT: SERVIDOR TCP (python3)
#
# COMO EXECUTAR?
# ?> python servidorTCP.py
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverPort = 30000 # porta a servir
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind(('',serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
serverIP=gethostbyname(gethostname())
print ('> servidor iniciado em %s:%d ...' % (serverIP,serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8') # codifica em utf-8
  print ('> mensagem recebida de %s -> %s' % (addr, sentence))
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor