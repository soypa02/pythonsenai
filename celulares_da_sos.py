print ("-" * 5 , "LOJINHA DA SOSO" , "-" * 5)
print ("""
1- SAMSUNG - R$ 5.500,00
2- IPHONE - R$ 2.800,00
3- XIAOMI - R$ 1.300,00
       
-----------------------
       
FRETE POR ESTADO:
MG : R$ 15
SP : R$ 10
RS : R$ 5
RJ : R$ 50        

 """)

cel = (input("qual o numero do produto que deseja?"))
sig = (input("qual estado seria o frete?"))

match cel: 
    case 1:
         cel = 5.500
    case 2:
          cel = 2.800
    case 3:
          cel = 1.300
    case _:
          print ("uai")


match sig : 
    case  ("RS") :
        sig = 5  








    # case "rs":
    #       sig = 5
    # case "MG" :
    #       sig = 15
    # case "mg" :
    #       sig =15
    # case "sp":
    #       sig= 10 
    # case "SP":
    #       sig =10 
    # case "rj" "RJ":
    #       sig = 50
    # case _:
    #       print ("uai")




print ("*" *10)
print (f"{sig} e {cel}" )

