l_nomes = [] 
def main(): 
    while True:
        CRUD = input('[C]Create(inserir um item)\n[R]Read(mostrar toda a lista)\n[U]Update (substituir um item)\n[D] Delete (deletar um item)\n[E] Exit\n').strip().upper() 
        if CRUD   == 'C': 
            create() 
        elif CRUD == 'R': 
            read() 
        elif CRUD == 'U': 
            update() 
        elif CRUD == 'D': 
            delete() 
        elif CRUD == 'E': 
            break 
        else: 
            input('Digite um valor válido')
def create ():  
    for x in range(int(input('Quantos nomes você quer digitar?'))):
        nome = input('Inserir nome: ').strip()
        l_nomes.append(nome)  
def read(): 
    print(l_nomes) 
def update(): 
    vlh_nome = input('Qual nome você quer mudar?').strip() 
    nv_nome = input('Para o que?').strip()
    local = l_nomes.index(vlh_nome)
    l_nomes[local] = nv_nome 
def delete(): 
    vlh_nome1 = input('Qual nome você quer apagar?').strip()
    local1 = l_nomes.index(vlh_nome1) 
    l_nomes.pop(local1) 
if __name__ == '__main__':
    main()