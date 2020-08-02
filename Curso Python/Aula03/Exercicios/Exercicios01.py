# Exercício Python #001 - Quebrando um número

# Exercício: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Primeiro Exemplo 

# num = float(input('Digite um Número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,int(num)))

# Segundo Exemplo

# import math
# num = float(input('Digite um Número: '))
# print('O valor digitado foi {} e a sua porção inteira é {}'.format(num,math.trunc(num)))

# Terceiro Exemplo

from math import trunc
num = float(input('Digite um Número: '))
inteiro = trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))