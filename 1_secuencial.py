
def cuadrado(numero):
	
	resultado = numero * numero
	
	print("El cuadrado de " + str(numero) + " es " + str(resultado) + "\n")

if __name__ == '__main__':

	numeros = [1,2,3,4]

	for numero in numeros:
		cuadrado(numero)

