import os
os.system("cls") 
#aula 02 -> variaveis, tipos e input 
#tipos de dados:
# string -> texto
# int -> inteiro 
# float -> quebrado (flutuante)

#declaraão de variaveis
escola = "senai"
#mostrando o valor da variavel no print
#concatenando com o +
print ("o nome da minha escola é" + escola)
#separando por parametro ,
print ("o nome da minha escola é" , escola)
#f string {} -> mostra o valor da viariavel dentro das aspas 
print (f"o nome da minha escola é {escola}") 

#exemplo de varivavel int 
numero = 100
print ("somando com 10=" , numero+10)
print ("subtraindo 5=", numero -5)
print ("dividindo por 2", numero /2)
print ("multiplicando por 10=" , numero *10)


nome = "soso"
idade = "15"
cpf= "123457487587484555584"

print ("meu nome é " + nome)
print ("minha idade é " + idade , "anos")
print ("este é meu cpf: " + cpf)

#input, guardar dados 
texto = input ("digite algo: ")
print ("voce digitou ...  " ,texto) 

print ("********* CADASTRO *********")
nome = input ("digite seu nome:")
cpf = input ("digite seu cpf:")
rg = input ("digite seu rg:")

print ("******** DADOS CADASTRADOS *********")
print ("nome: ", nome)
print ("cpf: " , cpf)
print ("rg: " , rg)
