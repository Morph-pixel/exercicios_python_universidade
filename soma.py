ct = 0
soma = 0
while True: 
    numero = int(input('qual o número?'))
    if numero == -1:
        break
    soma = soma + numero 

    ct += 1
print(f'Números digitados:{ct}\nSoma:{soma}')
