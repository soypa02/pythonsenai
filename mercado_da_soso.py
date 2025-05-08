import os
os.system("cls") 

print ("--------------SUPERMECADO-LEGAL--------------")
comprabacana = input ("o que voce precisa hoje?")
produto1 = float(input ("Qual o preço disto? "))
compralegal = input ("algo mais?")
produto2 = float(input("qual o preço disto?") )

descontolegal = 0.25 * produto1
descontobacana = 0.70 * produto2

# roud: arredonda os valores -> (valor, quantidade de casas decimais) 

print ("-------- CAIXA-LEGAL -------")
print (f"{comprabacana} tem 25% de desconto = {descontolegal}")
print (f"{compralegal} tem 70% de desconto = {descontobacana}")

valorlegal = round (produto1 - descontolegal, 2) 
valorbacana = round(produto2 - descontobacana, 2 ) 

print ("-------------------------------------")
print (f"O total da sua compra é de: R${valorbacana + valorlegal}" )
