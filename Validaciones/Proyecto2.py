import csv
import Validaciones as va
import Colision as col


#Lista para guardar los valores que lee del .CSV
List = []
ListIDs = []
ListXins = []
ListYins = []
ListXouts = []
ListYouts = []
ListTimes = []
ListSpeed= []

#Numero de campos requeridos de la lista
Campos = 7 

  
#Validacion de Campo, Recibe una Lista Que Representa a Los Campos de Un Avion
def check_campo(List):
    print ("\n___________________________________\n") 
    print ('-- Checkeando Avion :' + List[0] +'--')  
    count = 1 
    checkG = True

    if len(List)== Campos :
        for campo in List: 
            check = va.validate(campo,count)
            if check==False:
                checkG = False
            count = count + 1   
                      
    else :
          print('Campos insuficientes')
          checkG = False;          
    
    return (checkG)
     
    

def read():
    try:
        with open('estacion.csv', newline='') as f:
         reader = csv.reader(f)
         for row in reader:
          List.append(row)    
    except:
         print ('El archivo no existe')
   


def main():
    read()
    if not List:
      print ("No hay datos en el archivo")
    else :
        count = 0
        length = len(List)
        while (count != length):

         avion = List[count]

         ListIDs.append(avion[0])
         ListXins.append(float(avion[1]))
         ListYins.append(float(avion[2]))
         ListXouts.append(float(avion[3]))
         ListYouts.append(float(avion[4]))
         ListTimes.append(float(avion[5]))
         ListSpeed.append(float(avion[6]))

         #Si pasa
         if(check_campo(avion)):
            print()
            print ('--El Avion: ' + avion[0] + ' Fue Permitido\n Coordenadas Entrada (' + avion[1] + ','+ avion[2] +')' +
                                     '\n Coordenadas Salida (' + avion[3] + ','+ avion[4] +')' +
                                      '\n MinutoEntrada (' + avion[5] + ')'+
                                       '\n Velocidad (' + avion[6] + ')'
                )


         else:
          
            print ('--El Avion: ' + avion[0] + ' No puede ingresar a la zona') 
        
        
         count = count + 1


    elimina = col.colisiones(ListIDs,ListXins,ListYins,ListXouts,ListYouts,ListTimes,ListSpeed)
    print ('Elimina:' , elimina)

#llamada a funcion principal
main()    
