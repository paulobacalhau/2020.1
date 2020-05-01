outfile = open ("notas.txt", "w")
outfile.write ("Essas são as notas da prova\n")
for i in range(10):
    outfile.write (str(i) + "**" * i + "\n")
outfile.close()
print("Arquivo criado...")


#    print ("Vamos ler o que foi gravado")
#    infile = open ("notas.txt", "r")
#    linha = infile.read()
#    print (linha)

print ("Vamos ler o que foi gravado, linha a linha")
entrada = open ("notas.txt", "r")
linha = entrada.readline()
while linha != "":
     print (linha)
     linha = entrada.readline()
entrada.close()
