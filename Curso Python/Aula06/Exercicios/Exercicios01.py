# Exercício Python 01 - Aprovando Empréstimo

#Exercício:  01 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da Casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos =  int(input('Quantos anos de fincanciamento? '))
prestação = casa/(anos * 12)
minimo = salario * 30 / 100
print('Para pagar unma casa de R${:.2f} em {} anos '.format(casa,anos), end='')
print('A prestação será de {:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser CONCEDIDO !')
else:
    print('Emprestimo ! NEGADO !')
