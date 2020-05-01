def converte_em_dias (dia, mes, ano):
    data_em_dias = dia + mes * 30 + ano * 365
    return data_em_dias

### Pede valores da data atual
ano_atual = int ( input ("Informe o ano atual "))
mes_atual = int (input("Informe o mês atual "))
dia_atual = int (input("Informe o dia de hoje "))

data_atual_dias = converte_em_dias (dia_atual, mes_atual, ano_atual)
#print ("Data atual em dias", data_atual_dias )

### Pede ano, mes e dia do nascimento do animal
ano_nascimento = int (input("Informe o ano de seu nascimento "))
mes_nascimento = int (input("Informe o mês do seu nascimento "))
dia_nascimento = int (input("Informe o dia do seu nascimento "))

data_nascimento_dias = converte_em_dias (dia_nascimento, mes_nascimento, ano_nascimento)
# print ("Sua data de nascimento em dias e", data_nascimento_dias)

diferenca = data_atual_dias - data_nascimento_dias
print ("Sua idade em dias", diferenca)
ano_idade = diferenca / 365
print ("Você tem ", ano_idade, " de idade")