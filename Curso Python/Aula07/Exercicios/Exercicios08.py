#Exercício Python #08 - Detector de Palíndromo
# Exercício: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.


#Primeiro Exemplo

#frase = str(input('Digite uma frase: ')).strip().upper()
#palavra = frase.split()
#junto = ''.join(palavra)
#inverso = junto[:: -1]
#print('O inverso de {} é {}'.format(junto, inverso))
#if inverso == junto:
#    print('Temos um palindromo!')
#else:
#    print('A frase digitada não é um palindromo!')





#Segundo Exemplo

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
print('Você digitou a frase {}'.format(junto))
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')
