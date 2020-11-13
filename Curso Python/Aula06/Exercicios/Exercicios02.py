# Exercício Python #02 - Conversor de Bases Numéricas

# Exercício: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 
#
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {}'. format(num,bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é a {}'.format(num,oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é a {}'.format(num,hex(num)))
else:
    print('Opção invalida. ! TENTE NOVAMENTE !')
