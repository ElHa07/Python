#Exercício Python #02 - Jogo da Adivinhação v2.0

#Exercício: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10. ')
print('Será que você consegue adivinhar qual foi ? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Hum pensei em um numero maior... Tente mas dessa vez um numero maior.')
        elif jogador > computador:
            print('Hum pensi em um numero menor agora... Tente mais uma vez.')
print('Acertou miseravél com {} tentativas. Parabéns' .format(palpites))