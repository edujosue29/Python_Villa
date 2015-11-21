def colisiones(Id,Xin,Yin,Xout,Yout,Hora,Velocidad):
    Elimina=[]
    #COLISIONES DE LAS TRAYECTORIAS
    i=-1
    j=0
    
    while(i<len(Xin)-1):
        j=0
        i=i+1
                   
        while(j<len(Xin)-1):
            #Pendientes
            M1=float((Yout[i]-Yin[i])/(Xout[i]-Xin[i]))
            M2=float((Yout[j]-Yin[j])/(Xout[j]-Xin[j]))
            
            #Interseccion eje Y
            B1=Yin[i]-(M1*Xin[i])
            B2=Yin[j]-(M2*Xin[j])
            #misma trayectoria
            if((M1==M2) and (B1==B2)):
                #Mensaje misma trayectoria
                T1=Hora[i]
                T2=Hora[j]
            
            else: #Trayectorias diferentes
                
                #Intersección entre aviones
                XI=(B2-B1)/(M1-M2)
                YI= M1*XI+B1
                #distancia de intersección
                D1=(((YI-Yin[i])**2)+((XI-Xin[i])**2))**0.5
                D2=(((YI-Yin[j])**2)+((XI-Xin[j])**2))**0.5
                #tiempo de intersección
                T1=Hora[i]+(D1/Velocidad[i])
                T2=Hora[j]+(D2/Velocidad[j])
                #aceptar o rechazar vuelos
            if(i==j):
                T1=0
                T2=1
            if(T1==T2):
                
                if(Hora[i]<Hora[j]):
                    Elimina.append(j)

                else:
                    Elimina.append(j)

            j=j+1
                    
    return Elimina
    
