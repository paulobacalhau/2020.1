def soma (n1, n2):
   print ("A soma de ", n1 , " com n2 ", n2 , " eh ", (n1 + n2) )
   
num1 = int ( input ("Informe o primeiro numero ") )
num2 = int ( input ("Informe o segundo numero ") )
print ("A soma dos dois números eh ", (num1 + num2) )

print ("Agora usando a função que criei")
a = 0
while a < 5:
   a += 1
   soma ( num1 + a, num2 * a )





    
