#Curso Python #05 - Condições

#Nessa aula, vamos aprender como utilizar estruturas #condicionais simples e compostas nos seus programas #em Python.

#Condições
#Simples e Compostas.

#tempo = int(input('Quantos anos tem seu carro?'))

#if tempo <= 3:
#    print('carro novo !')
#else:
#    print('carro velho!')
#print('--FIM--')

#Segunda Versão

#nome = str(input('Qual é o seu Nome?'))
#if nome == 'Jefferson':
#    print('Que nome lindo você tem !')
#else:
#    print('Seu nome é tão comun!')
#print('Bom dia, {}'.format(nome))

#Terceira Versão

#n1 = float(input('Digite a primeira nota: '))
#n2 = float(input('Digite a segunda nota: '))
#m = (n1 + n2)/2
#print('A sua media foi: {:.1f}'.format(m))
#if m  >= 6.0:
#    print('A sua media foi boa ! VOCÊ CONCLUIU !')
#else:
#    print('Hum, você não conseguiu ! ESTUDE UM POUCO MAIS !')

#Quarta Versão

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi: {:.1f}'.format(m))
if m  >= 6.5:
    print('A sua media foi boa ! VOCÊ CONCLUIU !')
elif m <= 6.0:
    print('Quase ! tome mais, ! CUIDADO !')
else:
    print('Hum, você não conseguiu ! ESTUDE UM POUCO MAIS !')