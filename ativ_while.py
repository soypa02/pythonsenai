
# c = 1
# d = 1
# while c == d: 
#     a = int(input("senha?"))
#     if a == 1505 :
#         print ("certo")
#         c = 1
#     elif a == 9999:
#         c = 2 
#         print ("cabo")
#     else:
#         print ("erro")
#         c = 1
    

# import random
# e = 99
# i = 99
# while e == i :
#     a = random.randint(1,10)
#     b = int(input("numero"))
#     if b == a :
#         print ("acertou")
#         print (f"a maquina escolheu {a} e voce {b}")
#         i = 888
#     else :
#         print ("nao acertou")
#         print (f"a maquina escoelheu {a} e voce {b}")

# print ("------------CAIXA------------")
# print ("""  digite 1 para depositar
#           digite 2 para saque
#           digite 3 para conta
#           digite 4 para sair
#        """)
# saldo = 0
# op = 0
# while op != 4:
#     op= float(input("qq vc qr? "))
#     if  op == 1:
#         dep= float(input("quanto vc qr? "))
#         saldo = saldo+dep
#     elif op == 2: 
#         saq = float(input("quanto vc qr? "))
#         saldo = saldo-saq 
#     elif op==3:
#         print (f"seu saldo é {saldo}")
#     else : 
#         print("Seu burro eh uma das três opções")
# else :
#     print ("saiu do coiso")


# print ("-----------------------")
# print ("""  digite 1 para somar
#             digite 2 para multiplicar
#             digite 3 para ver qual é o maior
#             digite 4 para adicionar novos numeros
#             digite 5 para sair do programa 
#        """)

# n1= float(input("digite um numero:"))
# n2 = float(input("digite outro numero:"))
# op = int(input("qual opçao voce quer?"))

# while op != 5:
#     op = int(input("qual opçao voce quer?"))

#     if  op == 1 :
#             soma = n1 +n2 
#             print (f"a soma é {soma}")

#     elif op ==2:
#             print (f"a multiplicaçao de {n1} e {n2} é" , n1*n2)
    
#     elif op==3:
#             ma= max (n1,n2)
#             print (f"o maior numero entre {n1} e {n2} é {ma}")
    
#     elif op==4:
#             n1 = float(input("digite um novo numero:"))
#             n2 = float(input("digite um outro novo numero:"))
#     elif op==5:
#           break
#     else :
#         print ("uai so")

# else :
#     print ("saiu do coiso")


print ("-----------CAIXA-------------")
valor = int(input("quanto voce deseja sacar em especie?"))
print ("notas disponiveis: 100, 50, 20, 10, 5 e 1 ")
print ("digite -1 para sair!")

n100 = valor //100
print (n100)
valor = valor - (n100*5)
print (valor, n100)

