maior_valor =-999999999
menor_valor = 999999999
ct = 0
soma = 0
while True:
    valor = int(input('Valor inteiro:'))
    ct += 1 
    soma = soma + valor
    if valor == 0: 
        break 
    if valor > maior_valor: 
        maior_valor = valor
    if valor < menor_valor:
        menor_valor = valor
print(f'Soma:{soma}\nQuantidade de números digitados:{ct}\nMenor valor:{menor_valor}\nMaior valor:{maior_valor}')