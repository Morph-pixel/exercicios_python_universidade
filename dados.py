import random
import time
c1 = 0
c2 = 0 
c3 = 0 
c4 = 0 
c5 = 0
c6 = 0
for numero in range(1,13):
    time.sleep(2)
    numero_sorteado = random.randint(1,6)
    print(numero_sorteado)
    if numero_sorteado == 1:
        c1 += 1
    elif numero_sorteado == 2:
        c2 += 1
    elif numero_sorteado == 3:
        c3 += 1
    elif numero_sorteado == 4:
        c4 += 1
    elif numero_sorteado == 5:
        c5 += 1
    else: 
        c6 += 1
print(f'Qt1: {c1}\nQt2: {c2}\nQt3: {c3}\nQt4: {c4}\nQt5: {c5}\nQt6: {c6}')