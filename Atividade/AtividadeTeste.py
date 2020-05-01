from unittest import TestCase

def soma(num1, num2):
    return (num1+num2)
    
class TestSoma(TestCase):
    def test_Soma(self):
        resultado = soma(1,2)
        self.assertEquals(3,resultado)
        resultado = soma(2,3)
        self.assertEquals(4,resultado)
