'''
Elaborar um programa que determine a idade atual de uma pessoa (em anos, meses e dias).
'''
def converte_data_em_dias(data):
    dia, mes, ano = (data.split("/"))
    ano_dias = int(ano) * 365
    mes_dias = int(mes) * 30
    dias     = int(dia)
    return (ano_dias + mes_dias + dias)

### Pede-se o nome da pessoa
nome  = input("Entre com o seu nome ")

#Pede-se a data de nascimento
data_nascimento = input("Entre com a sua data de nascimento (DD/MM/AAAA) ")
dt_nascimento_em_dias = converte_data_em_dias ( data_nascimento )

### Pede-se a data atual
data_atual  = input("Entre com a data atual (DD/MM/AAAA) ")
dt_atual_em_dias = converte_data_em_dias ( data_atual )

idade_em_dias = dt_atual_em_dias - dt_nascimento_em_dias
idade_em_anos = idade_em_dias // 365
idade_em_dias -= ( idade_em_anos * 365 )
idade_em_meses = ( idade_em_dias ) // 30
idade_em_dias -= ( idade_em_meses * 30 )

print( "{0}, você tem {1:3} anos, {2:2} meses e {3:2} dias de idade "
      .format( nome , idade_em_anos, idade_em_meses, idade_em_dias ) )
