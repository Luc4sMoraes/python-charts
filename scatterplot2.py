import matplotlib.pyplot as plt 

x1 = [1, 3, 5, 7 , 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]
z = [2000, 55, 400, 330, 100]
 
titulo = "Scatterplot"
eixox = "Eixo X"
eixoy = "Eixo Y"
#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="meus pontos", color='#000', marker=".", s=z)
plt.plot(x,y,color="#000fff", linestyle=":")
plt.legend()
#plt.show()
plt.savefig("Figura 1.png", dpi=300)