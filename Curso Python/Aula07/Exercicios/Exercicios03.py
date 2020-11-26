#Exercicios em Python
#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#Primeiro Exemplo

soma = 0
c = 0
for cont in range(0, 500, 2):
    if cont % 3 == 0:
        soma += cont
        c = c + 1
print('A somos de todos os {} valores solicitados é {}!'.format(c,soma))