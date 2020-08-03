# Exercício Python #003 - Seno, Cosseno e Tangente

# Exercício: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Primeiro Exemplo
# import math
# an = float(input('Digite o ângulo que você deseja: '))
# seno = math.sin(math.radians(an))
# print('O ângulo de {} tem o SENO de {:.2f}'.format(an,seno))
# cosseno = math.cos(math.radians(an))
# print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an,cosseno))
# print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,tangente))

# Segundo Exemplo

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2}'.format(an,cosseno))
tangente = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2}'.format(an,tangente))