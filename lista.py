lista = [] 
while True:
    numero = int(input('Digite um número, digite 0 para encerrar').strip())
    if numero == 0:
        break 
    lista.append(numero)
for item in lista:
    print(item)  
print(f'{lista}\nTamanho:{len(lista)}\nMáx:{max(lista)}\nMin:{min(lista)}\nSoma:{sum(lista)}\n') 
pesquisa = int(input('Qual valor você quer procurar?')) 
if pesquisa in lista: 
    print(f'{pesquisa} está na lista.\nPosição:{lista.index(pesquisa)}') 
else: 
    print(f'{pesquisa} não está na lista') 
lista.insert(1,33)  
lista.sort()
lista.reverse() 
print(lista) 

