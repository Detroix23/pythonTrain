"""
V1 - 2022
V1.1 - 2025

"""


import time



nbr = 1
divisibilitee = 0
print('Start run')
nbrs = []

try:
  while True:

  #Test de premiereté
    for testeur in range(1, nbr+1):
      if nbr % testeur == 0:
        divisibilitee = divisibilitee + 1

    if divisibilitee == 2:
      nbrs.append(nbr)

    nbr = nbr + 1
    divisibilitee = 0
except KeyboardInterrupt:
  print(nbrs[-1])
finally:
  print(nbrs[-1])
