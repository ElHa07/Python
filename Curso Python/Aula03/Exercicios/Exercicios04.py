# Exercício Python #004 - Sorteando um item na lista

# Exercício: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Primeiro Exemplo

#import random
# n1 = str(input('Primeiro Aluno: '))
# n2 = str(input('Segundo Aluno: '))
# n3 = str(input('Terceiro Aluno: '))
# n4 = str(input('Quarto Aluno: '))

# lista = [n1, n2, n3, n4]
# escolhido = random.choice(lista)
# print('O Aluno escolhido foi {}'.format(escolhido))

# Segundo Exemplo

from random import choice
n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
n5 = str(input('Quinto Aluno: '))

lista = [n1, n2, n3, n4,n5]
escolhido = choice(lista)
print('O Aluno escolhido foi {}'.format(escolhido))