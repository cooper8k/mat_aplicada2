import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import fsolve

# ejercicio 1 


# funciones 
def s(x):
    return-1.6*x**2+1.3*+141.3

def r(x):
    1.4*x**2-5.6*x+12.6
    

# encontrar intercepcion
def inter(x):
    return -551 



x=np.linspace(0,1000,500)
solucion=fsolve(inter,x)
print(f'solucion es {solucion[0]:.1f}')
