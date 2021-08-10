import matplotlib.pyplot as plt 

x1 = [1, 3, 5, 7 , 9]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]
 
titulo = "Scatterplot"
eixox = "Eixo X"
eixoy = "Eixo Y"
#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="meus pontos", color='r')
plt.plot(x,y)
plt.legend()
plt.show()