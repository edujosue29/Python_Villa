#Variables de rango
rango_min = -125
rango_max = 125
punto_entrada = 25 

#Validaciones para punto de entrada
def validation(campo):
    if campo.isnumeric() :
        if( (int(campo)%punto_entrada==0) and
            (int(campo)>=rango_min) and
           ( int(campo)<=rango_max )):
            return True
        else :
          return False
    else :
          return False
  
#Validaciones para el tiempo 
def validation_time(campo):

        return True
 
def validation_speed(campo):
    
       return True

# Validaciones  a cada campo

    #Chequear Xin ######################################################
def validate(campo,count):
    check = True
    if count == 2:
        if ( validation(campo)) :
         print('Campo Xin Perm',campo)
        else :
            print('Campo Xin N-Perm',campo)
            check = False
     #Chequear Yin #####################################################       
    if count == 3:
        if ( validation(campo)) :
         print('Campo Yin Perm',campo)
        else :
            print('Campo Yin N-Perm',campo)
            check = False  
     #Chequear Xout ####################################################        
    if count == 4:
         if ( validation(campo)) :
            print('Campo Xout Perm',campo)
         else :
            print('Campo Xout N-Perm',campo)
            check = False
     #Chequear Yout ####################################################       
    if count == 5:
        if ( validation(campo)) :
            print('Campo Yout Perm',campo)
        else :
            print('Campo Yout N-Perm',campo)
            check = False
     #Chequear Time ####################################################        
    if count == 6:
        if ( validation_time(campo)) :
            print('Campo Time Perm',campo)
        else :
            print('Campo Time N-Perm',campo)
            check = False
    if count == 7:
        if ( validation_speed(campo)) :
            print('Campo Speed Perm',campo)
        else :
            print('Campo Speed N-Perm',campo)
            check = False

    return check