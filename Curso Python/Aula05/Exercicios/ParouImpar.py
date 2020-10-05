# Exercício Python #03 - Par ou Ímpar

#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Primeiro Exemplo

numero = int(input('Me diga um número qualquer: '))
resultados = numero % 2
if resultados == 0:
    print('O numero {} é PAR' .format(numero))
else:
    print('O numero {} é IMPAR' .format(numero))
print('! FIM !')