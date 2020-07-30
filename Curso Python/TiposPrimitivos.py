# Curso Python #01 - Tipos Primitivos e Saída de Dados

#Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str(). Além disso, veremos como fazer as primeiras operações com a função print() do Python.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

s = n1 + n2

print('A Soma entre {} e {} vale {} ' .format(n1, n2, s))