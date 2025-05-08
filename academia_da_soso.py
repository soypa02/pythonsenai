print ("-----" , "CALCULANDO SEU IMC" , "-----")
peso = float(input("digite seu peso:").replace(",", ".")) 
alt = float(input("digite sua altura:").replace(",", "."))  

imc = peso/(alt*alt)

if imc <= 17: 
    print ("muito abaixo do peso!")
elif imc <18.49:
    print ("abaixo do peso!")
elif imc <24.99:
    print ("peso normal!")
elif imc <29.99:
    print ("acima do peso!")
elif imc <34.99:
    print("obesidade I")
elif imc < 39.99:
    print ("obesidade II")
else: 
    print ("obesidade III")
