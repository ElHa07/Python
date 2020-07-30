# Exercício Python #002 - Dissecando uma Variável
# Faça um programa que leia algo pelo teclado e mostre, na tela o seu tipo primitivo e todas as informações possiveis sobre ele.add()

a = input('Escreva seu Nome: ')
b = int(input('Digite sua Idade: '))

print('O tipo primitivo desse valor é', type(a))
print('Só tem espaço ? ', a.isspace())
print('É um númnero ?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em Maiusculas', a.isupper())
print('Está em Minusculas', a.islower())
print('Está Capitalazada', a.istitle())