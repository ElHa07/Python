#Exercício Python #04 - Custo da Viagem

#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

# Primeiro Exemplo
distancia = float(input('Qual é a distancia da sua Viagem? '))
print('Você está prestes a começar uma viagem de {}Km' .format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('È o preço da sua viagem sera de R${:.2f}'.format(preço))
#
#
#