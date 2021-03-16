import wave
import numpy as np
import matplotlib.pyplot as plt

#carcar archivo wav en la variable
gm = wave.open('good-morning.wav', 'r')
ga = wave.open('good-afternoon.wav', 'r')

bonk = wave.open('bonk.wav', 'r')
pop = wave.open('pop.wav', 'r')

#obtener todos los fromas del objeto wave
frames_gm = gm.readframes(-1)
frames_ga = ga.readframes(-1)

frames_bonk = bonk.readframes(-1)
frames_pop = pop.readframes(-1)

#mostrar ek resultado de frames
#print(frames_gm[:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida_gm = np.frombuffer(frames_gm, dtype='int16')
ondaconvertida_ga = np.frombuffer(frames_ga, dtype='int16')

ondaconvertida_bonk = np.frombuffer(frames_bonk, dtype='int16')
ondaconvertida_pop = np.frombuffer(frames_pop, dtype='int16')

#Imprime los 10 primeros valores de la onda.
#print(ondaconvertida_gm[:10])

framerate_gm = gm.getframerate()
framerate_ga = ga.getframerate()

framerate_bonk = bonk.getframerate()
framerate_pop = pop.getframerate()

print(framerate_gm)
print(framerate_ga)

print(framerate_bonk)
print(framerate_pop)

time_gm = np.linspace(start=0,stop=len(ondaconvertida_gm)/framerate_gm, num=len(ondaconvertida_gm))
time_ga = np.linspace(start=0,stop=len(ondaconvertida_ga)/framerate_ga, num=len(ondaconvertida_ga))

time_bonk = np.linspace(start=0,stop=len(ondaconvertida_bonk)/framerate_bonk, num=len(ondaconvertida_bonk))
time_pop = np.linspace(start=0,stop=len(ondaconvertida_pop)/framerate_pop, num=len(ondaconvertida_pop))

print(time_gm[:10])
print(time_ga[:10])

print(time_bonk[:10])
print(time_pop[:10])

#generacion de la grafica
plt.title('Good morning vs Good afternoon')

#etiqueta de los ejes
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud')

#Agregar informacion de las ondas
plt.plot(time_gm, ondaconvertida_gm, label='Good afternoon')
plt.plot(time_ga, ondaconvertida_ga, label='Good afternoon', alpha=0.75)

plt.plot(time_bonk, ondaconvertida_bonk, label='Bonk', alpha=0.5)
plt.plot(time_pop, ondaconvertida_pop, label='Cat Pop', alpha=0.25)

plt.legend()
plt.show()