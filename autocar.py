print ( "."*10 , "REAJUSTE AUTOCAR" , "."*10 )
print (r"""
  `;-.          ___,        
  `.`\_...._/`.-"`        
    \        /      ,     
    /()   () \    .' `-._ 
   |)  .    ()\  /   _.'  
   \  -'-     ,; '. &lt;     
    ;.__     ,;|   &gt; \    
   / ,    / ,  |.-'.-'    
  (_/    (_/ ,;|.&lt;`       
    \    ,     ;-`        
     &gt;   \    /           
    (_,-'`&gt; .'            
jgs      (_,'             

""")


s1 = float(input("qual é o seu salario?"))

if s1 <= 2799.99:
    print ("seu salario irá aumentar e 20%")
    nv = (s1 * 0.20) + s1 
elif s1 <= 2800.00:
    print ("seu salario aumentará em 15%")
    nv = (s1 * 0.15) + s1
elif s1 <= 7000.00 or s1 <=14999.99:
    print ("seu salario aumentará em 10%")
    nv = (s1 * 0.10) +s1
else :
    print ("seu salario aumentará em 5%")
    nv = (s1 * 0.5) + s1

print (f"seu salario agora é {nv}")