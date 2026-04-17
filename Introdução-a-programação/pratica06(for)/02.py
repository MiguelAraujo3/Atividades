#Esse programa vai ler a nota de 40 alunos e verificar e imprimir os seguintes requisitos
#- Média da turma;
#- Quantidade de alunos aprovados;
#- Quantidade de alunos na final;
#- Quantidade de alunos reprovados.
media = 0
aprov = 0
final = 0
reprov = 0
for i in range(1, 41):
    nota = int(input(f'Digite a nota do aluno {i}: '))
    media += nota
    if nota >= 70:
        aprov += 1
    elif nota >= 40:
        final += 1
    else:
        reprov += 1
media = media/40
print(f'A nota média da turma é {media:.0f} e tem {aprov} alunos aprovados, {final} alunos na final e {reprov} alunos reprovados')
