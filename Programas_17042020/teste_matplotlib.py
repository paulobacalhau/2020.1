import matplotlib.pyplot as plt # grafico

#labels = ['Alex', 'Gezineia', 'Weslley', 'Lucas', 'Marcelo']
#sizes = [7,5,2,4,8]

#fig1, ax1 = plt.subplots()

#ax1.pie (sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
#ax1.axis('equal')
#plt.show()

# Definindo variáveis
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 5, 6, 8, 4, 8]
 
# Criando um gráfico	
plt.scatter(x, y, label = 'Pontos', color = 'b', marker = '*', s = 100)
plt.legend()
  
plt.show()

