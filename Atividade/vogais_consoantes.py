def vogais (lista):
    lista_vogais = lista
    contVogais = 0
    contCons = 0
#for para percorrer a lista a procura de vogais e consoantes
    for vogaisCons in lista_vogais:
        if(vogaisCons in "aeiouAEIOU"):
       
           contVogais += 1
        if(vogaisCons in "bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVWXZ"):

           contCons += 1

    return print("A palavra {} tem {} vogais e {} consoantes"
              .format(lista_vogais, contVogais, contCons))

    

def preencherVogais():
    
    print("Contador de vogais e consoantes!\n\n")

    lista_vogais = []


    lista_vogais = (input("Digite uma palavara: "))

    funcVogais = vogais(lista_vogais)




preencherVogais()    
