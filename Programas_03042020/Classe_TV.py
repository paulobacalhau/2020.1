class Televisao:
    def __init__(self):
        # print ("Init")
        self.canal = 4
        self.ligada = False
        self.volume = 10

    def botao_power(self):
        if self.ligada == False:  # not self.ligada
            self.ligada = True
        else:
            self.ligada = False
        pass

    def aumentar_canal(self):
        if self.ligada:
            self.canal += 1

    def diminuir_canal(self):
        pass

    def aumentar_volume(self):
        pass

    def diminuir_volume(self):
        pass

tv = Televisao()                                 # criei o objeto
#print ("Volume {}".format(tv.volume))
print ("1 - Está ligada = {}".format(tv.ligada)) # perguntei se está ligada
print ("Antes de aumentar Canal {}".format(tv.canal))
tv.botao_power()
tv.aumentar_canal()
print ("Depois de aumentar Canal {}".format(tv.canal))

# print ("1 - Está ligada = {}".format(tv.ligada)) # perguntei se está ligada
# tv.botao_power()                                 # executei o metodo botao_power()
# print ("2 - Está ligada = {}".format(tv.ligada)) # perguntei novamente se estava ligada

