#Estrutura de Repetição While
#Metdoso de Repetição

# Primeiro Metodo de Repetição FOR
# o For não é possivel usa-lo quando eu não sei o quanto valores serão. 
#for c in range(0, 10):
#    print(c)
#print('FIM!')

#Segundo Metodo de Repetição WHILE
# While serve para situações diversas quando eu sei quantos valores são e quando não sei quantos valores serão!#

#c = 1
#while c < 10:
#    print(c)
#    c += 1
#print('FIM!')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar [S/N] ? ')).upper()
print('FIM!')
