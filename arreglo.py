arreglo1 = [1,3,3,1]
arreglo2 =[0,0,0,0,0,0]

for i in range (3,7):
    aux =0
    suma =0
    arreglo2[0]=1
    arreglo2[i + 1 ]=1
    for j in range (0,(i)):
        suma =0
        suma = arreglo1[j]+arreglo1[j + 1]
        print (suma)
        u = j + 1
        #print (" u "+str (u)+" "+str(suma))
        arreglo2[u]=suma
      
    print ("arreglo 2 ")
    print (arreglo2)  
    arreglo1 = arreglo2.copy()  # Aquí usamos .copy() para evitar modificar el mismo objeto

    print ("arreglo 1 ")

    print(arreglo1)
         
 
        
 
              #for m  in range (0,(i+1)):
            #print(f"Elemento en la posición {m}: {arreglo2[m]}")


    if (i==4):
        break

    
    
     
       
         
  
    