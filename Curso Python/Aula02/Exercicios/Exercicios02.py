# Exercício Python #001 - Dobro, Triplo, Raiz Quadrada

# Exercício Python 001: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1 = int(input('Digite um Número: '))

d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)

print('O valor mostrado é {} o dobro é {} o triplo {} e raiz quadrada é {:.1f} !'.format(n1, d, t, r))