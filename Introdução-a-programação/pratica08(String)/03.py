#Esse programa le um texto e exibi todos os caracteres desse
#texto convertidos para maiúsculo. (SEM USAR UPPER())
#
frase = input('Informe uma frase: ')

for letra in frase:
    if ord(letra) > 96 and ord(letra) < 123:
        print(chr(ord(letra)-32), end='')
    else:
        print(letra, end='')
