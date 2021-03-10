import wave
import numpy as np

#carcar archivo wav en la variable
gm = wave.open('good-morningMan.wav', 'r')

#obtener todos los fromas del objeto wave
frames = gm.readframes(-1)

#mostrar ek resultado de frames
print(frames[:10])

#Convierte el audio good morning de bytes a enteros
ondaconvertida = np.frombuffer(frames, dtype='int16')

#Imprime los 10 primeros valores de la onda.
print(ondaconvertida[:10])