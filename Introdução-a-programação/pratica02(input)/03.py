#programa para obtém do usuário a quantidade de alunos aprovados e a quantidade de alunos reprovados em uma disciplina.
#Ele calcula e imprime a porcentagem de alunos aprovados.
#quantidade de alunos aprovados
qaa = int(input("Digite aqui a quantidade de alunos aprovados: "))
#quantidade de alunos reaprovados
qar = int(input("Digite aqui a quantidade de alunos reaprovados: "))
#quantidade total de alunos
qta = qaa + qar
#taxa de aulos aprovados
taa = (qaa/qta)*100
print(f"A taxa de alunos aprovados nessa disciplina é: {taa:.1f}", end = "%")
