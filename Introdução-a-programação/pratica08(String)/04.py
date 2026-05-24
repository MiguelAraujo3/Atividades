#Esse programa lê um texto e remove todos os espaços em branco que estão em excesso. Ou seja, deixar apenas um único espaço em branco entre
#as palavras do texto.
frase = str(input("Digite uma frase: "))
print(frase)
frase = frase.strip()
print(frase)
