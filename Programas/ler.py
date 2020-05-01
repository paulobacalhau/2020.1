arquivo_entrada = open ("notas.txt", "r")
linha = arquivo_entrada.readline().strip()
linha_sep = linha.split()

while linha != "":
     print (linha)
     linha_sep = linha.split()
     print (linha_sep)
     linha = arquivo_entrada.readline().strip()

arquivo_entrada.close()
