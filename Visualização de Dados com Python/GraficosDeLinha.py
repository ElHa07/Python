# Conhecer a biblioteca MATPLOTLIB PYPLOT

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,1]

#Titulo
titulo = "grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel("Eixox")
plt.ylabel("Eixosy")

plt.plot(x,y)
plt.show()