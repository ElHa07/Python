# Exercício Python 07 Números Primos
# Exercício Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('', end=' ')
    else:
        print('', end=' ')
    print('{}'.format(c), end=' ')
print('O número {} foi divisivel {} vezes'.format(núm, tot))
if tot == 2:
    print('É por isso ele é PRIMO!')
else:
    print('É por isso ele NÂO É PRIMO!')