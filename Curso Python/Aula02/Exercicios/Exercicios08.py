# Exercício Python #008 - Pintando Parede

# Exercício: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Insira a Largura da parede: '))
alt = float(input('Insira a Altura da parede: '))
área = larg * alt
tinta = área / 2
print('Sua parede tem a dimensão de {} x {} e sua area é de {}m²'.format(larg,alt,área))
print('Para pintar essa parede, você precisará de {:.1f}L de tinta !'.format(tinta))