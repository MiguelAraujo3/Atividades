#########TESTANTO CÓDIGOS, COMO TIPOS DE NÚMERICOS, FORMATAÇÃO DE TEXTO E VARIÁVEIS###
faturamento = float(input("Digite o valor de faturamento: "))
custo =  float(input("Digite o valor de custo: "))
lucro = faturamento - custo
imposto = 0.15

texto = f"O custo foi de R${custo:.2f} e o faturamento foi de R${faturamento:.2f} então o lucro foi de R${lucro:.2f} e a taxa de imposto é {int(imposto*100)}%"

print (texto)

email, idade, nome, numero = input("Digite seu email, idade, nome e número: ").split()
idade = int(float(input("Digite sua idade: ")))
nome = input("Digite seu nome: ")
numero = float(input("Escreva um número com 5 casas decimais: "))
idade = int(idade)
numero = float(numero)
email = email.lower().strip()
print("Meu nome", nome, "Minha idade", idade, "Meu email", email, sep = ": ")
print("Seu email: {} Sua idade: {} Seu nome: {}".format(email, idade, nome))
print(f"Seu email: {email} Sua idade:{idade} Seu nome: {nome}")
print(f"Número:{numero:.5f} Número:{numero:.4f} Número:{numero:.3f} Número: {numero:.2f} Número: {numero:.1f}") 

#servidor
posicao = email.find("@") + 1
servidor = email[posicao:]
print(f"Servidor do email: {servidor}")