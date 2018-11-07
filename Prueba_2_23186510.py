#~ Ejercicio 1

print "Por favor indique la cantidad de numeros que quieres asignar"
numeros = input()
lista = []
for i in range (numeros):
    numero2= raw_input ("Digame el numero " + str(i+1) + " ")
    lista.append(numero2)

print "La Primera lista es: " , lista

nuevalist = []
inicio = 0

for i in lista:
	inicio = inicio + int(i)
	nuevalist.append(inicio)
	
print "Los resultados de las sumas es: " , nuevalist	

#~ Ejercicio 2

tupla = (1,2,3,4,5,1,2,3)

print 'Ingrese el numero a consultar'
consulta= input ()

for i in tupla:

if consulta = i
	print i 
	


