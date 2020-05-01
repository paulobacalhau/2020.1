'''
Elaborar um programa para calcular o preço de venda de um determinado produto
considerando impostos e uma margem de lucro pretendida.
(memória de cálculo, compartilhada no drive da disciplina,
 no formato Excel, como preço de venda)
'''
### A seguir pedem-se todos os valores/impostos
Valor_Custo = float (input("Informe o valor de custo do produto : "))
Imp_ICMS = float (input("Informe o valor do imposto do ICMS : "))
Imp_PIS = float (input("Informe o valor do imposto do PIS : "))
Imp_COFINS = float (input("Informe o valor do imposto do COFINS : "))
Margem_Lucro = float (input("Informe a margem de lucro pretendida : "))

### Agora convertemos os impostos e margem para percentual dividindo por 100
Perc_ICMS = Imp_ICMS / 100
Perc_PIS = Imp_PIS / 100
Perc_COFINS = Imp_COFINS / 100
Perc_Margem = Margem_Lucro / 100

### Agora calculamos o valor agregado de impostos, somando todos os percentuais
Total_Agregado = Perc_ICMS + Perc_PIS + Perc_COFINS + Perc_Margem

## Calcula-se o fator a ser aplicado no valor de custo para achar o valor de venda
Fator = 1 - Total_Agregado

## Calculamos o valor de venda
Valor_Venda = Valor_Custo / Fator

print("Tem-se o valor de venda: {0:6.2f}  para o valor de custo informado: {1:6.2f} "
      .format(Valor_Venda, Valor_Custo))

### Agora calculamos os impostos sobre o valor de venda

Valor_ICMS = Valor_Venda * Perc_ICMS
print("{0:6.2f}% de ICMS sobre {1:6.2f} eh igual a: {2:6.2f} "
      .format(Imp_ICMS, Valor_Venda, Valor_ICMS ))

Valor_PIS = Valor_Venda * Perc_PIS
print("{0:6.2f}% de PIS sobre {1:6.2f} eh igual a: {2:6.2f} "
      .format(Imp_PIS, Valor_Venda, Valor_PIS))

Valor_COFINS = Valor_Venda * Perc_COFINS
print("{0:6.2f}% de COFINS sobre {1:6.2f} eh igual a: {2:6.2f} "
      .format(Imp_COFINS, Valor_Venda, Valor_COFINS))

Valor_Lucro = Valor_Venda * Perc_Margem
print("{0:6.2f}% de LUCRO sobre {1:6.2f} eh igual a: {2:6.2f} "
      .format(Margem_Lucro, Valor_Venda, Valor_Lucro))
vTotal = Valor_ICMS + Valor_PIS + Valor_COFINS + Valor_Lucro
print("O total de incidencias sobre o valor de venda {0:6.2f} eh {1:6.2f} "
      .format(Valor_Venda, vTotal))
print ("C.Q.D.")