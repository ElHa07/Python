# Exercicio em Python 01

#Exercicios: Faça um programa que mostre na tela uma contagem regreciva para o estouro de fogos de artificios, indo de 10 até 0, com uma pausa de 1 segundo entre eles

from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('FELIZ ANO NOVO !')
    