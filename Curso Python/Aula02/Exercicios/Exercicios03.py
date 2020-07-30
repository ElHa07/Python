# Exercício Python #003 - Média Aritmética

# Exercício: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite sua primeira Nota: '))
n2 = float(input('Digite sua segunda Nota: '))

media =  (n1+n2)/2

print('A media entre {} e {} é igual a {:.1f}! '.format(n1,n2,media)) 