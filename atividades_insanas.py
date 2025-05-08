import os
os.system("cls") 
print ("MULTIPLICAÇÃO!")
n1 = float(input ("digite um numero:") )
n2 = float(input ("digite outro numeor:"))

resultado = n1*n2
print (f"a multipliçao de {n1} + {n2} = " , resultado)

print("-----------------")

print ("SOBRE O NUMERO!")
numerolegal = float(input ("digite um numero:") )
antecessor = numerolegal - 1 
sucessor = numerolegal + 1 
print (f"antecessor: {antecessor}")
print (f"sucessor: {sucessor}")
print("-----------------")

print ("SUA IDADE!")
ano = float (input ("digite o ano do seu nascimento: "))
idade= 2025 - ano 
print (f"sua idade é: {idade} anos!")
print("-----------------")

