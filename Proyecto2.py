#import numpy as np

def main():

    try:
        Id,Xin,Yin,Xout,Yout,Hora,Velocidad= np.loadtxt('estacion.csv',delimiter=',',unpack=True,
                                  dtype='str')

    except Exception, e:
        print str(e)
    Xin=map(int,Xin)
    Yin=map(int,Yin)
    Xout=map(int,Xout)
    Yout=map(int,Yout)
    Hora=map(int,Hora)
    Velocidad=map(int,Velocidad)
    
    print Yout
##    Xin[i]=int(Xin[i])
##    Yin[i]=int(Yin[i])
##    Xout[i]=int(Xout[i])
##    Yout[i]=int(Yout[i])
##    Hora[i]=int(Hora[i])
##    Velocidad[i]=int(Velocidad[i])
##    print Velocidad
