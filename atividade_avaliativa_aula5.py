listaNotasAluno = []
listaNotasTurma = []

quantAlunos=int(input('Digite a quantidade de alunos: '))

for c in range(1, quantAlunos+1):
    listaNotasAluno.clear()
    nome = str(input('Nome do aluno: '))
    for c in range(1, 4):
        nota = float(input(f'Digite a {c}º nota: '))
        listaNotasAluno.append(nota)
        listaNotasTurma.append(nota)
    print('='*15)
    print(f'{nome}:')
    print('Notas: ')
    for n in listaNotasAluno:   
        print(n)
    mediaAluno = sum(listaNotasAluno)/3
    print(f'Media: {mediaAluno:.2f}')
    if mediaAluno >=7:
        print('O aluno foi aprovado!')
    else:
        print('O aluno foi reprovado!')
    print('='*15)

mediaTurma = sum(listaNotasTurma)/len(listaNotasTurma)
print(f'A média da turma é de {mediaTurma:.2f}')
