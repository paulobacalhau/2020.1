class Calculadora:
    def __init__(self, num1, num2):
        self.valor1 = num1
        self.valor2 = num2

    def somar_self(self):
        return self.valor1 + self.valor2

    def somar (self, numero1, numero2):
        return numero1 + numero2

    def subtrair (self, numero1, numero2):
        return numero1 - numero2

    def multiplicar (self, numero1, numero2):
        return numero1 * numero2

    def dividir (self, numero1, numero2):
        return numero1 / numero2
# print (__name__)
if __name__ == '__main__':
    # num1 = int (input("Digite o 1 valor "))
    # num2 = int (input("Digite o 2 valor "))
    # soma = somar (num1, num2)
    # subtracao = subtrair (num1, num2)
    # multiplicacao = multiplicar (num1,num2)
    # divisao = dividir(num1, num2)
    # print ("A soma de {} e {} = {}".format(num1, num2, soma))
    # print ("A subtracao de {} e {} = {}".format(num1, num2, subtracao))
    # print ("A multiplicacao de {} por {} = {}".format(num1, num2, multiplicacao))

    # nova_calc = Calculadora()
    # print ("A soma pela nova calc ", nova_calc.somar(24,20))
    # outra_calc = Calculadora()
    # print ("A subtracao pela outra ", outra_calc.subtrair(20,4))

    geane = Calculadora(15,25)
    print (geane.somar_self())