def conta_vogais(parametro1):
    pass

def conta_consoantes(parametro2):
    pass

def imprime_vogais (parametro3):
    if parametro3 in "aeiou":
        print ("E vogal =", parametro3)

nome = input ("Informe o seu nome ")
for letra in nome:
#    if  letra in "aeiou":
#        print (letra)
     imprime_vogais (letra)
