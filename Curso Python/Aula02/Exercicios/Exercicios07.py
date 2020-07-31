# Exercício Python #007 - Conversor de Moedas

# Exercício: Crie um programa que leia quanto a conversão do dolar para Reais.

dolar = float(input('Quantos dolares você tem US$? '))
real = dolar * 5.22
print('Sua conversão de US$ {} para R$ é {:.2f} Reais!'.format(dolar,real))
