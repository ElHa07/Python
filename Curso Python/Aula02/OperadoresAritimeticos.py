# Curso Python #02 - Operadores Aritméticos

#Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.

#Primeira Versão 

# n1 = int(input('Digite um Valor: '))
# n2 = int(input('Outro Valor: '))
# print('A soma vale {}'.format(n1+n2))


#Segunda Versão 

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.1f}'.format(s,m,d), end=' ')
print('Divisão inteira é {}, e potencia {}!'.format(di,e))
