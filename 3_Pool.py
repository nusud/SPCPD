# -*- coding: utf-8 -*-

# para saber la cantidad de procesadores disponibles abro una terminal interactiva de python
# import multiprocessing
# multiprocessing.cpu_count()

import time
from multiprocessing import Pool

def suma_cuadrados(numero):
	s = 0
	for i in range(numero):
		s += i * i
	return s

def suma_cuadrados_con_mp(numeros):
	
	tiempo_inicio = time.time()

	# instancio un objeto de la clase Pool
	# si no paso ningun argumento a Pool, usará la máxima cantidad de procesadores
	# disponibles en el sistema
	p = Pool()
	# ahora mapea (asigna) cada proceso a un procesador disponible en nuestro sistema
	p.map(suma_cuadrados, numeros)

	p.close()
	p.join()

	tiempo_fin = time.time() - tiempo_inicio

	print("Procesar " + str(len(numeros)) + " llevó " + str(tiempo_fin) + " utilizando mp")

def suma_cuadrados_sin_mp(numeros):

	tiempo_inicio = time.time()

	resultado = []

	for i in numeros:
		resultado.append(suma_cuadrados(i))

	tiempo_fin = time.time() - tiempo_inicio

	print("Procesar " + str(len(numeros)) + " llevó " + str(tiempo_fin) + " sin utilizar mp")

if __name__ == "__main__":

	numeros = range(10000)
	
	suma_cuadrados_con_mp(numeros)
	
	suma_cuadrados_sin_mp(numeros)
