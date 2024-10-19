import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import fsolve

#funciones lineales
##x= 42
#print(costoLuz(x))

#def parZapatos(x):
#    return(35000-9000)*x-120000
#print(parZapatos(215))

#def velocidad (t):
#    return 40*t +1.6
#print(velocidad(89))

#def valor(x):
#    return 599990-55000 * x
#print(valor(8))


# funciones y sus aplicaciones 

#def nose (x):
#    return (-2*x**3)+(27*x**3)-(108*8 +200)
#:.......................................................


#def r(x):
#    return -1.5*x**2 +11.5*x -15


#def g(x):
#    return 1.58*x**4 -19.17*x**3 + 80.92*x**2 -139.33*x +85

#x = np.arange(0,50,0.01)
#plt.plot(x,r(x),color ='r',label ='r(x)')
#plt.plot(x,g(x),color ='g',label='g(x)')

#plt.xlim(0,6)
#plt.ylim(-10,10)

#plt.title('comparacion entre las funciones  g(x)y r(x)')
#plt.grid(True)
#plt.legend
#plt.show()

def inte(x):
    return g(x)-r(x)

#x=np.linspace(0,15,15)
#decimal=2
#solucion = np.around(fsolve(inte,x),decimal)
#intercepcion = np.unique(solucion)

#print(f'los puntos de intercepcion de las funciones estan en x={intercepcion}')

#w:..........................................
#2

def h(x):
    return 2 *(x-2)**2

def i(x):
    return x+1

x=np.arange(-5,100,0.01)
plt.plot(x,h(x),color ='m' ,label = 'h(x)')
plt.plot(x,i(x),color ='y',label = 'i(x)')

plt.xlim(-5,5)
plt.ylim(-2,10)

plt.title('comparacion entre las funciones h(x)y i(x)')
plt.grid(True)
plt.legend()
plt.show()

solucion = np.around(fsolve(inte,x),decimal =2)
intercepcion = np.unique(solucion)


print(f'los puntos de intercepcion es {intercepcion}')
print(1)