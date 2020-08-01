import matplotlib.pyplot as plt

x1 = [2,3,7,1,0]
y1 = [2,3,5,7,10]

x2 = [6,5,4,3,2]
y2 = [2,3,5,7,0]

#Titulo
titulo = "Grafico de Barras 2"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel("Eixox")
plt.ylabel("Eixosy")

#plt 
plt.bar(x1,y1, label="Grupo 1")
plt.bar(x2,y2, label="Grupo 2")
plt.show()