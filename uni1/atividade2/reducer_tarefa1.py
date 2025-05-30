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
curr_word = None
curr_count = 0
palavras = []

# Process each key-value pair from the mapper
for line in sys.stdin:
  # Get the key and value from the current line
  word, count = line.split('\t')
  # Convert the count to an int
  count = int(count)
  # If the current word is the same as the previous word,
  # increment its count, otherwise print the words count
  # to stdout
  if word == curr_word:
    curr_count += count
  else:
    if curr_word:
      palavras.append({
        "palavra": curr_word,
        "cont": curr_count
      })
    curr_word = word
    curr_count = count

# ordenando em ordem decrescente as palavras pela key "cont" do dicionario
ordenado = sorted(palavras, key=lambda x: x['cont'], reverse=True)

for elemento in ordenado:
  print(f'{elemento["palavra"]} {elemento["cont"]}')
