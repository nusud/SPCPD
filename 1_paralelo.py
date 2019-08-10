
import os
from multiprocessing import Process, current_process

def cuadrado(numero):

	resultado = numero * numero

	nombre_del_proceso = current_process().name

	print(nombre_del_proceso)

	print("El cuadrado de " + str(numero) + " es " + str(resultado) + "\n")

if __name__ == '__main__':
	
	procesos = []

	numeros = [1,2,3,4]
	
	for numero in numeros:
		proceso = Process(target=cuadrado, args=(numero,))
		procesos.append(proceso)
		proceso.start()
