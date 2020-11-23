#Exercício Python #09 - Gerenciador de Pagamentos

#Exercício: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOS GARCIAS '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou  mais no cartão''')
opção = int(input('Qual é a opção: '))
if opção == 1:
    total = preco - (preco * 10 / 100)
elif opção == 2:
    total = preco - (preco * 5 / 100)
elif opção == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em  2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'. format(totalparc,parcela))
else:
    total = preco
    print('OPÇÃO ERRADA POR FAVAOR ESCOLHA UMA OPÇÃO VALIDA!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco,total))