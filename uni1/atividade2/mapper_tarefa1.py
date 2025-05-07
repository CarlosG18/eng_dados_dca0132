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

#!/usr/bin/env python
import sys
import io

# decodificando as palavras para o padrão utf-8
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

# criamos uma lista vazia para adicionar as palavras e depois realizar a ordenação com todas as palavras
words_list = []

#!/usr/bin/env python
import sys
# Read each line from stdin
for line in sys.stdin:
  # Get the words in each line
  words = line.split()
  # Generate the count for each word
  for word in words:
    # adiciononamos na lista de palavras com a trasformação da palavra para minusculo
    words_list.append(word.lower())

# é ultilizado o metodo interno do python para ordenação com a lista de todas as palavras
words_list.sort()
for word in words_list:
  # realizado o print no formato palavra<TAB>1
  print ('{0}\t{1}'.format(word, 1))
