#Exercício Python #01 - Jogo da Adivinhação

#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Primeiro Exemplo

#from random import randint
#computador = randint(0,5)
#print('Pensei no numero {}'.format(computador))


#Segundo Exemplo

#from random import randint
#computador = randint(0,5) #Faz o computador "PENSAR"
#print('=X=' * 30)
#print('Vou pensar em um número entre 0 e 5. ! TENTE ADIVINHAR SE FOR CAPAZ !')
#print('=X=' * 30)
#jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar !
#if jogador == computador:
#    print('! TSC. ! Você conseguiu me  VENCER... ! SORTE DE PRICIPIANTE QUERO VER VOCÊ GANHAR DUAS VEZES SEGUIDAS....!')
#else:
#    print('! GANHEI ! Eu pensei no número {} e não no {} ! TREINE MAIS ANTES DE QUERER ME DESAFIAR MUHAHAHA !'.format(computador,jogador))


#Terceiro Exemplo

from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador "PENSAR"
print('=X=' * 30)
print('Vou pensar em um número entre 0 e 5. ! TENTE ADIVINHAR SE FOR CAPAZ !')
print('=X=' * 30)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar !
print('Hum deixe me ver....')
sleep(3)
if jogador == computador:
    print('! TSC. ! Você conseguiu me  VENCER... ! SORTE DE PRICIPIANTE QUERO VER VOCÊ GANHAR DUAS VEZES SEGUIDAS....!')
else:
    print('! GANHEI ! Eu pensei no número {} e não no {} ! TREINE MAIS ANTES DE QUERER ME DESAFIAR MUHAHAHA !'.format(computador,jogador))