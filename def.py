def calctri(base,altura):
    return (base * altura)/2 
if __name__ == '__main__':
    bat = float(input('Qual a altura do triângulo?')) 
    at = float(input('Qual a base do triângulo?'))  
    print(f'A área do triângulo é {calctri(bat,at):.0f}')
