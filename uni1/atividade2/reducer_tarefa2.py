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
# SCRIPT: REDUCER (python3)
#

#!/usr/bin/env python
import sys
curr_ip = None
curr_count = 0
ips = []

# Process each key-value pair from the mapper
for line in sys.stdin:
  # Get the key and value from the current line
  ip, count = line.split('\t')
  # Convert the count to an int
  count = int(count)
  # If the current word is the same as the previous word,
  # increment its count, otherwise print the words count
  # to stdout
  if ip == curr_ip:
    curr_count += count
  else:
    if curr_ip:
      # adicionando o dict de ip e cont na lista de ips
      ips.append({
        "ip": curr_ip,
        "cont": curr_count
      })
    curr_ip = ip
    curr_count = count

# ordenando em ordem decrescente as palavras pela key "cont" do dicionario
ordenado = sorted(ips, key=lambda x: x['cont'], reverse=True)

# printando os ips na ordem descrecente de acesso
for elemento in ordenado:
  print(f'{elemento["ip"]} {elemento["cont"]}')
