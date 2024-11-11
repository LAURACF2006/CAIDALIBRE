import numpy as np
h=200 # Altura inicial 
g=9.8 #Aceleracion gravedad tierra
#Array de tiempos usando numpy
t=np.linspace(0, np.sqrt(2*h/g), num=100)
#Calcula la posición vertical en cada espacio de tiempo
y=h-0.5*g*t**2
#Calcula la diferrencia en posición
dif=-np.diff(y) #como sale negativo pongo -np.diff en vez de np.diff
#Calcula la media de las diferencas
calc_dif=np.mean(dif) 
#Mostramos los resultados 
print(f"altura inicia: {h} metros")
print(f"aceleracion de la gravedad: {g} metros por segundo")
print(f"tiempo de caida: {t[-1]:.2f} segundos")
print(f"diferencia de posición entre pasos de tiempo consecutivos: {dif}")
print(f"distancia media de caida entre intervalos de `puntos de referencia: {calc_dif: .2f} metros")
