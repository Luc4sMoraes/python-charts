#Crescimento da polulação BR 1980-2016
#datasus

import matplotlib.pyplot as plt

dados = open("p.csv").readlines()

x = []
y = []

for i in range(len(dados)):
  if i != 0:
    linha = dados[i].split(";")
    x.append(int(linha[0]))
    y.append(int(linha[1]))
#print(x)

plt.bar(x, y, color="#e4e4e4")
plt.plot(x, y, color='k', linestyle="--")


plt.title("Crescimento População BR 1980-2016")
plt.xlabel("Ano")
plt.ylabel("Pop. x100.000.000")

plt.savefig("populaçãoBR.png",dpi=300)