# Exercício Python #02 - Conversor de Bases Numéricas

# Exercício: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal. 

#Primeiro Exemplo
#
#num = int(input('Digite um número inteiro: '))
#print(''' Escolha uma das bases para conversão:
#[ 1 ] converter para BINARIO
#[ 2 ] converter para OCTAL
#[ 3 ] converter para HEXADECIMAL''')

#opção = int(input('Sua opção: '))
#if opção == 1:
#    print('{} convertido para BINARIO é igual a {}'. format(num,bin(num)[:2]))
#elif opção == 2:
#    print('{} convertido para OCTAL é a {}'.format(num,oct(num)[:2]))
#elif opção == 3:
#    print('{} convertido para HEXADECIMAL é a {}'.format(num,hex(num)[:2]))
#else:
#    print('Opção invalida. ! TENTE NOVAMENTE !')

#Segundo Exemplo
n = int(input('Digite um valor decimal: '))
escolha = int(input('Digite: \n- 1 para binário: \n- 2 para octal: \n- 3 para Hexadecimal: \nEscolha sua opção pelo Número: '))
if escolha == 1:
    print('O Número {} decimal equivale a {} em Binário'.format(n, bin(n).strip('0b')))
elif escolha == 2:
    print('O Número {} decimal equivale a {} em Octal'.format(n, oct(n).strip('0o').upper()))
elif escolha == 3:
    print('O Número {} decimal equivale a {} em Hexadecimal'.format(n, hex(n).strip('0x').upper()))
else:
    print('Você escolheu uma opção inválida.')