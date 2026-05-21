#Esse programa solicita ao usuário a criação de uma senha e
#verifica se ela atende a um conjunto de critérios de segurança pré-definidos, a seguir:
#• Ter no mínimo 8 caracteres;
#• Conter pelo menos uma letra maiúscula;
#• Conter pelo menos duas letra minúscula;
#• Conter pelo menos um número;
#• Conter pelo menos dois caractere especial.
def min_char (senha: str) -> str:
    if len(senha) < 7:
        print("A senha deve ter pelo menos 8 caracteres")
        return False
    return True
def maisc (senha: str) -> str:
    total_minusculas = sum(1 for caracter in senha if caracter.islower()) 
    if total_minusculas < 2:
        print ("A senha deve ter pelo menos duas letras minúsculas")
        return False
    return True
def minus (senha: str) -> str: 
    if senha.islower():
        print ("A senha deve ter pelo menos uma letra maiúscula")
        return False
    return True
def special (senha: str) -> str: 
    total_especial = sum(1 for caracter in senha if caracter.isalnum())
    if total_especial < 2:
        print ("A senha deve ter pelo menos dois caracteres especiais")
        return False
    return True
def num (senha: str) -> str: 
    if senha.isalpha():
        print ("A senha deve ter pelo menos um número")
        return False
    return True
##############
while True:
    senha = str(input("Digite sua senha: "))
    min_char(senha)
    maisc(senha)
    minus(senha)   
    special(senha)
    num(senha)
    if  min_char(senha)  and maisc(senha) and minus(senha) and special(senha) and num(senha):
        print("Senha Válida")
