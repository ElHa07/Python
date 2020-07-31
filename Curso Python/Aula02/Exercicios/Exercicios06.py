# Exercício Python #006 - Conversor de Moedas

# Exercício: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

#Primeira Parte

# real = float(input('Quanto dinheiro você tem na Carteira? '))
# dolar = real / 5.43
# print('Com R${} você pode comprar US${:.2f} Dollar! '.format(real,dolar))

# Segunda Parte

 #real = float(input('Quanto dinheiro você tem na Carteira? '))
# Euro = real / 6.82
# print('Com R${} você pode comprar ER${:.2f} Euro!'.format(real,Euro)) 

# Terceira Parte
print('='*60)
print('! BEM VINDO A NOSSA LOJA DE CAMBIO !')
print('='*60)

real = float(input('Quanto dinheiro você tem na Carteira? '))
dolar = real / 5.43
Euro = real / 6.82

print('Com R${} você pode comprar US${:.2f} Dollares! '.format(real,dolar))
print('Com R${} você pode comprar ER${:.2f} Euros!'.format(real,Euro))

print('='*60)
print('! OBRIGADO POR COMPRAR EM NOSSA LOJA')
print('='*60)