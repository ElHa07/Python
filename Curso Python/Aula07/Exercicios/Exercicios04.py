# Exercício Python 04
# Exercício : Refaça o DESAFIO, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-=' * 25)
tab = int(input('Digite um número para saber a sua Tabuada: '))
for c in range(0, 11):
    print('{} x {:2} = {}'.format(tab,c,tab*c))
print('-=' * 25)
print('FIM!')
    
