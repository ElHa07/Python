#Faça um Programa que peça as 4 notas bimestrais e mostre a média

nota1 = float(input('Digita a Primeira Nota: '))
nota2 = float(input('Digita a Segunda Nota: '))
nota3 = float(input('Digita a Terceira Nota: '))
nota4 = float(input('Digita a  Quarta Nota: '))

media =  (nota1 + nota2 + nota3 + nota4) / 2
print('A sua media foi: {:.1f}'.format(media))
