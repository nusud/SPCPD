# declaro el encoding para poder utilizar acentos en los comentarios
# -*- coding: utf-8 -*-

import os
import time
from multiprocessing import Process, current_process

# ahora voy a iterar sobre una lista de números e introduzco una pausa para poder
# llegar a visualizar los procesos paralelos en administrador de procesos del 
# sistema operativo

def cuadrado(numeros):
	for numero in numeros:
		time.sleep(0.5)
		resultado = numero * numero
		print("El cuadrado de " + str(numero) + " es " + str(resultado) + "\n")

if __name__ == '__main__':

	# inicializo una lista de procesos vacía:
	procesos = []

	# creo una lista de números de 0 al 99
	numeros = range(100)
	
	# inicializo 50 procesos para procesar los 100 números
	for i in range(50):
		proceso = Process(target=cuadrado, args=(numeros,))
		procesos.append(proceso)
		proceso.start()

	# me aseguro que todos los procesos que inicié hayan terminado
	for proceso in procesos:
		proceso.join()

	print("Multiprocesamiento terminado")
