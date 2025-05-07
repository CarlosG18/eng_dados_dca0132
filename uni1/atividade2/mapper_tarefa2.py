# ██████╗  ██████╗ █████╗
# ██╔══██╗██╔════╝██╔══██╗
# ██║  ██║██║     ███████║
# ██║  ██║██║     ██╔══██║
# ██████╔╝╚██████╗██║  ██║
# ╚═════╝  ╚═════╝╚═╝  ╚═╝ UFRN 2024
#
# PROF CARLOS M D VIEGAS (C)
# carlos.viegas '@' ufrn.br
#
# ----------------------------------------------- 
#
# SCRIPT: MAPPER (python3)
#

import re 

# criando um regex para pegar apenas os endereços de ips
regex = r'^\d{1,3}(?:\.\d{1,3}){3}'

# lista para armazenar os ips
ips_list = []

#!/usr/bin/env python
import sys
# Read each line from stdin
for line in sys.stdin:
  # Get the words in each line
  words = line.split()
  # Generate the count for each word
  for word in words:
    # aplicando o regex em cada palavra obtida da linha
    if re.findall(regex, word):
      # colocando os ips na lista de ips
      ips_list.append(word)

# ordenando os ips para a saida está correta para o reduce
ips_list.sort()

# printando os ips
for ip in ips_list:
  print ('{0}\t{1}'.format(ip, 1))
