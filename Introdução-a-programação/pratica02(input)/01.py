#Esse programa obtém do usuário a quantidade aulas de uma disciplina e a quantidade de faltas que um aluno obteve.
#Calcula e imprime a frequência desse aluno
aula = int(input("Quantas aulas você tem dessa disciplina? " ))
falta = int(input("Quantas faltas você obitve nessa disciplina? "))
presenca = aula-falta
frequencia = (presenca/aula)*100

    
print(f'Sua frequência é {frequencia:.1f}', end = '%')
