print ("*" *5, "jOGO PREDA PAPER E TIC TIC" , "*" *5)
print ("""
Escola qual voce quer!
pedra = 1
papel =2 
tesoura =3 

""")

escolha = float(input("digite aqui!:"))


import random
maquina = random.randint(1,3)
papel = 1
pedra = 2
tesoura = 3 

match escolha:
    case 1:
        escolha = papel
    case 2:
        escolha= pedra 
    case 3:
        escolha = tesoura
    case _:
        print("uai")

print (f"voce escolheu {escolha} e o roberto escolheu {maquina}")

