#1.	Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
#A quantidade de valores digitados;
#A soma dos valores digitados;
#A média aritmética dos valores digitados;
#E a quantidade de valores digitados maior que 20.

ct = 0 
ct20 = 0
soma = 0
print('Aperte enter quando já tiver todas as notas')
while True: 
    nr = input('Qual a média?').strip()
    if nr == '':
        break
    nr = float(nr)
    if nr > 20:
        ct20 += 1
    ct += 1
    soma = soma + nr 
print(f'Quantidade de números digitados:{ct}\nQuantidade de números acima de 20 digitados:{ct20}\nSoma:{soma}\nMédia:{soma/ct:.2f}')