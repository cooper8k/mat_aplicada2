import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def a(n):
    return 0.01*n**2+0.5*n+2

print(f'holis {a(1300)}')

n=np.arange(0,2950,1)
plt.plot(n,a(n))
plt.title('relacion')
plt.xlabel('cantidad de elementos')
plt.ylabel('tiempo')
plt.grid(True)
plt.show()


def tiempo(n):
    return 0.01*n**2+0.5*n -21598

n=np.linspace(0,500,10)

solucion = fsolve(tiempo,n)

print(f'solucion {solucion[0]:.0f}')