#Esse programa recebe do usuário a média semestral e a nota da avaliação final e imprime a média final conforme a fórmula
#Média Semestral
ms = int(input("Digite aqui sua Média Semestal: "))
#Avaliação final
af = int(input("Digite aqui a nota da Avaliação Final: "))
#Média Final
mf = int(((6*ms)+(4*af))/10)

print(f"Sua média final é: {mf}")
