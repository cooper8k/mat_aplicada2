import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tiker 

# problema 1
def f(t):
    return t * 100
#45 seg 
    print(f' para los 45 seg se transmiten {f(45)} megabits')
# 1.5 min
    print(f' para los 1.5 minutos se transmiten {f(90)} megabits')
# una hora 
    print(f' para la hora {f(60*60)} megabits')

#....................................................................................

# problema 2

    for i in range(0,1100,100):
        print(f'{i} s: {f(i)} megabits')
#....................................................................................


#problema 3

    def latencia (e):
        return round(e * 1.2)

    print(f'Cuando la latencia estimada es 200 milisegundo, la latencia real es {latencia(200)} milisegundos aproximadamente.')
    print(f'Cuando la latencia estimada es 149 milisegundo, la latencia real es {latencia (149)} milisegundos aproximadamente.')
    print(f'Cuando la latencia estimada es 74 milisegundo, la latencia real es {latencia(74)} milisegundos aproximadamente.')

#....................................................................................

# problema 4

#1- funcion para calcular el largo del cable
def g(t):
    return 1.85 * t

#3- dominio contexrualizado de la funcion
    t=6600/1.85
    print(f'{t:.1f}')
#dom g(t) : [0;3.567.6]

# 4  grafico

    t = np.arange(0, 3569 ,1)

    plt.plot(t,g(t))

    plt.title('relacion entre el largo del cable de instalacion y el tiempo trascurrido ')
    plt.xlabel('tiempo transcurrido (horas)')
    plt.ylabel('largo del cable instalado (km)')

    plt.grid(True)
    plt.show()

#5 

# ultilizando la funcion definida en el ejercicio (1)

    tiempo_1=148
    tiempo_2=2300

    print(f'Transcurridas {tiempo_1} horas, se han instalado {g(tiempo_1)} km de cable y \n transcurridas {tiempo_2} se han instalado {g(tiempo_2)} kilometros de cable.')


#6 entonces g(t)=3.480
#  entonces $$3.480 = 1,85 t$$ $$\frac{3.480}{1,85} = t$$

    t = 3480/1.85

    print(f'Si se han instalado 3.480 kilometros de cable, es porque han trabajado {t:.1f} horas aproximadamente.')


#....................................................................................
#problema 5


# grafico de la funcion
    tiempo = np.arange(0, 15, 0.1)
    metro = 0.4 * tiempo
    bus = 0.3 * tiempo

    plt.plot(tiempo, metro, label = 'Metro')
    plt.plot(tiempo, bus, label = 'Bus')

    plt.title('Relación entre la distancia recorrida y el tiempo ')
    plt.xlabel('Tiempo (minutos)')
    plt.ylabel('Distancia recorrida (km)')
    plt.legend()
    plt.grid(True)

    plt.show()

    # 2 extremo superior del dominio

    t = 1.2 * 9 + 0.5 * 8

    print(f'el extremo superior es {t:.1f}')




#....................................................................................

import matplotlib.pyplot as plt
import numpy as np

tiempo = np.arange(0, 15, 0.1)
# aca np.array dice que quiero ir del 0 al 15 en 0.1 en 0.1
metro = 0.4 * tiempo
bus = 0.3 * tiempo

plt.plot(tiempo, metro, label = 'Metro')
plt.plot(tiempo, bus, label = 'Bus')

plt.title('Relación entre la distancia recorrida y el tiempo ')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Distancia recorrida (km)')
plt.legend()
plt.grid(True)

plt.show()

