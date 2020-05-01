'''
Elaborar um programa que conte a quantidade de vogais e a
quantidade de consoantes de uma string qualquer
(preferencialmente com o uso de funções).
'''
def conta_vogais( texto_informado ):
    '''
    Esta funcao retorna a quantidade de vogais em um
    texto qualquer passado como parametro
    '''
    nContador = 0                    # cria uma variável local para contar
    for letra in texto_informado:
        if letra.upper() in "AEIOU":  # Verifica se a letra convertida para maiúscula está contida na string de vogais
            nContador += 1
    return nContador

def conta_consoantes( texto_informado ):
    '''
    Esta funcao retorna a quantidade de consoantes em um
    texto qualquer passado como parametro
    '''
    nContador = 0                                    # cria uma variável local para contar
    for letra in texto_informado:
        if letra.upper() in "BCDFGHJKLMNPQRSTVXWYZ":  # Verifica se a letra convertida para maiúscula está contida na string de consoantes
            nContador += 1
    return nContador

texto = input ("Entre com um texto qualquer ")
nVogais = conta_vogais( texto )
nConsoantes = conta_consoantes( texto )
print("O texto informado: {} , tem {} vogais e {} consoantes"
      .format(texto, nVogais, nConsoantes))