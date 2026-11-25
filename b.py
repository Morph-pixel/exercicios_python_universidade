import random
palavra = ['bola','rap','Mark']
escolhida = random.choice(palavra)
letra = input('Diga uma letra').split()
if letra in escolhida:
    print('Está dentro, parabéns')
elif letra not in escolhida:
    print('Está fora, tente da próxima vez') 
print(escolhida)
    