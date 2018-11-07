"""
Ejercicios 1
Crea una funcion que calcule el factorial de un numero pasado por parametros 

Respuesta 1
def factorial (numero, *numeros):
	valor=numero
	for i in xrange(1,numero):
		valor*=i
	return valor 

valor= factorial(input("Ingrese el Numero Para calcular el Factorial:"   ))
print valor
"""





"""
Ejercicio 2
Crear una funcion que dados dos numeros mostrara todos los numeros que hay entre ellos

Respuesta 2
"""




"""
Ejercicio 3
Escriba una funcion que pida la anchura y la altura de un rectangulo y 
el caracter a utilizar en el dibujo:
Anchura del rectangulo: 5
Altura del Rectangulo: 3
Caracter a utilizar: 0
0 0 0 0 0
0 0 0 0 0	
0 0 0 0 0

Respuesta 3
"""

anchura = int(input("Anchura del rectangulo: "))
altura = int(input("Altura del rectangulo: "))
#caracter = int(input("Caracter para el rectangulo"))
for i in range(altura):
	for j in range(anchura):
		print(i,j)
print()


"""
Ejercicio 4
Mencione al menos 5 comandos de git y describa para que funcionan

Respuesta 4
1- git status = se utiliza para verificar el estatus de los archivos de la carpeta local en relacion
con la carpeta en git hub
2- git commit = se utiliza para comentar el cambio realizado en los archivos
3- git add =  su usa para agregar los archivos de la carpeta local 
4- git clone =    se utiliza para clonar el repositorio a un nuevo directorio
5- checkout = Cambiar de rama o restaurar los archivos del árbol de trabajo
"""
