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
# SCRIPT: CLIENTE TCP (python3)
#
# COMO EXECUTAR?
# ?> python clienteTCP.py <endereco-ip-do-servidor>
#

# importacao das bibliotecas
from socket import *
import sys
import time

# definicao das variaveis
serverName = str(sys.argv[1])
serverPort = 30000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = 'container id (hostname) ' + gethostname() + ' / ip ' + gethostbyname(gethostname())
print ('> enviando para o servidor -> %s' % sentence)
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
time.sleep(1)
clientSocket.close() # encerramento o socket do cliente
time.sleep(2)