alunos = 0 
media = 0
print('Aperte enter quando já tiver todas as notas')
materia = input('Qual matéria?')
print(materia)
while True: 
    nota = input('Qual a média?').strip()
    if nota == '':
        break
    nota = float(nota)
    alunos = alunos + 1
    media = media + nota 
media_alunos = media/alunos
if media_alunos%2 ==0:
    print(f'Matéria:{materia}\nSoma:{media}\nQuantidade de alunos:{alunos}\nMédia:{media/alunos:.2f}')
