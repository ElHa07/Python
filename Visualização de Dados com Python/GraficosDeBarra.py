import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,0]

#Titulo
titulo = "grafico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel("Eixox")
plt.ylabel("Eixosy")

plt.bar(x,y)
plt.show()