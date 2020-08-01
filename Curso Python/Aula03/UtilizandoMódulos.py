# Curso Python #003 - Utilizando Módulos

# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

# Primeiro Pate

# import math
# num = int(input('Digite um Número: '))
# raiz = math.sqrt(num)
# print('A raiz do {} é igual a {:.2f}!'.format(num,raiz))

# Segunda Parte

# from math import sqrt
# num = int(input('Digite um Número: '))
# raiz = sqrt(num)
# print('A raiz de {} é igual a {:.1f}'.format(num,raiz))

#Terceira Parte

# import random 
# num = random.random()
# print(num)

# Quarta Parte

# import random
# num = random.randint(1,10)
# print(num)

# Quinta Parte

import emoji
print(emoji.emojize("Olá Mundo :earth_americas:", use_aliases=True))