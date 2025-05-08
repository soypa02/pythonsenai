import os
os.system ("cls")

#estruturas condicionais IF ELSE (ELIF)
# switch caase -> (match case) escolha caso. A partir da 3.10v
#match --:
#   case --:

# linguagem = 90

# match linguagem:
#     case "python":
#                 print("ez")
#     case "java":
#                 print ("doente")
#     case "c#":
#                 print ("massa")
#     case "js":
#                 print ("sou do verdinho")
#     case "html":
#                 print ("aa")
#     case 10 :
#                 print ("entrou aq")
#     case _ :
#                 print ("outro caso") 

nu = 0 
nu = int(input("digite um numero entre 1 e 7: "))

match nu : 
    case 1:
         print("dom")
    case 2:
         print ("seg")
    case 3:
        print ("ter")
    case 4:
        print ("quarta") 
    case 5:
        print ("quinta")
    case 6:
         print ("sexta")
    case 7:
         print ("sabado")   
    case _:
          print ("uai")
          

