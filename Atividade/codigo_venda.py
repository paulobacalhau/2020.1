def venda():
    valor_icms = float(input('Entre com a taxa de icms em porcentagem: '))
    valor_pis = float(input('Entre com a taxa de de pis em porcentagem: '))
    valor_cofins = float(input('Entre com  a taxa do cofins em porcentagem: '))
    valor_margem = float(input('Entre com a porcentagem de margem de lucro deseja: '))
    valor_produto = float(input('Entre com o valor de custo do produto: '))
    calc_venda(valor_icms,valor_pis,valor_cofins,valor_margem,valor_produto)

def calc_venda(valor_icms,valor_pis,valor_cofins,valor_margem,valor_produto):
    soma_taxa= valor_icms+valor_pis+valor_cofins+valor_margem
    fator_calc= (1-(soma_taxa/100))*100
    valor_venda= valor_produto/(fator_calc/100)
    icms= valor_icms*valor_venda
    pis= valor_pis*valor_venda
    cofins= valor_cofins*valor_venda
    margem_lucro= (valor_margem/100)*valor_venda
    return print('margem de lucro: {:.2f}, preço de venda: {:.4f}'.format(margem_lucro,valor_venda))




venda()
