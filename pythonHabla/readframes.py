import wave

#carcar archivo wav en la variable
gm = wave.open('good-morningMan.wav', 'r')

#obtener todos los fromas del objeto wave
frames = gm.readframes(-1)

#mostrar ek resultado de frames
print(frames[:10])