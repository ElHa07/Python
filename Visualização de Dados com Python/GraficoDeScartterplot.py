# Visualização de dados em Python
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]

titulo = "Scatterplot: Graficos De Dispersão"
eixox = "Eixo X"
eixox = "Eixo Y"

plt.title(titulo)
plt.xlabel("eixox")
plt.ylabel("eixoy")

plt.scatter(x,y, label="Meus Pontos", color="g", marker="h", s=100)
plt.plot(x,y)
plt.legend()
# plt.show()
plt.savefig('figura1.png')