def soma(nr1,nr2):
    return nr1 + nr2 
def subtrai(nr1,nr2):
    return nr1 - nr2 
def main():
    prim = int(input('Qual o primeiro número?'))  
    seg = int(input('Qual o segundo número?')) 
    sinal = input('+ ou -?').strip()
    if sinal == '+': 
        print(soma(prim,seg))
    else: 
        print(subtrai(prim,seg)) 
if __name__ == '__main__': 
    main()