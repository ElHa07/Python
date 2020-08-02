# Exercício Python #002 - Catetos e Hipotenusa

#  Exercício: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# Primeiro Exemplo

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

# Segundo Exemplo

#import math
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = math.hypot(co, ca)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

# Terceiro Exemplo

from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai merdi {:.2f}' .format(hi))