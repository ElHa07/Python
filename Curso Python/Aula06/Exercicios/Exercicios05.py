print('-='* 40)
print('Exercício Python 05 - Aquele clássico da Média')
print('-='* 40)
#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

print('-='* 40)
nome = str(input('Qual é o seu Nome: '))
nota1 = float(input('Digite sua Primeira Nota: '))
nota2 = float(input('Digite sua Segundo Nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media >= 5:
    print('Hum, você ficou de !RECUPERAÇÂO! vai precisar estudar MAIS ! {}'.format(nome))
elif  media < 5:
    print('Sinto muito por você ter sido, ! REPROVADO ! {}'.format(nome))
elif media >= 7:
    print('MEUS PARABÉNS  VOCÊ FOI ! APROVADO !')
print('-='* 40)