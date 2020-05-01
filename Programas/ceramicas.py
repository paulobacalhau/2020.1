comprimento = float( input ("Informe o comprimento da sala ") )
largura = float ( input ("Informe a largura da sala ") )
larg_ceramica = float ( input ("Informe a largura da cerâmica em metros ") )

area_sala = comprimento * largura

area_ceramica = larg_ceramica * larg_ceramica

quant_ceramicas = area_sala / area_ceramica

print ( "Necessitamos de ", quant_ceramicas )
