def data_Nasc():
    ano_nasc = int(input('Entre com ano de nascimento: '))
    mes_nasc = int(input('Entre com mes de nascimento: '))
    dia_nasc = int(input('Entre com dia do nascimento: '))
    ano_atual = int(input('Entre com ano atual: '))
    mes_atual = int(input('Entre com mes atual: '))
    dia_atual = int(input('Entre com dia atual: '))
    data_Calcular(ano_atual,mes_atual,dia_atual,ano_nasc,mes_nasc,dia_nasc)

def data_Calcular(ano_atual,mes_atual,dia_atual,ano_nasc,mes_nasc,dia_nasc):
    atual_dia= 365*ano_atual+mes_atual*30+dia_atual
    nasc_dia= 365*ano_nasc+mes_nasc*30+dia_nasc
    #print('dias2 {}'.format(atual_dia))
    subtracao= atual_dia-nasc_dia
    ano1= subtracao/365.25
    mes1= (subtracao%365.25)/30
    dia1= (subtracao%365.25)%30
    return print('ano: {}, mes: {}, dia: {}'.format(ano1,mes1,dia1))




data_Nasc()
