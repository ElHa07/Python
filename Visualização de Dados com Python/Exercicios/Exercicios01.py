# Estudo de caso: crescimento da população brasileira

# Neste estudo de caso, criaremos um gráfico do crescimento da população brasileira.

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y)
plt.show()