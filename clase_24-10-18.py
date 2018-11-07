"""
lista = [('hola', 'don pepito'), ('hola', 'don jose'), ('Buenos', 'dias')]
dicc = {}

for i in lista:
	if not i[0] in dicc.keys():
		dicc[i[0]] = [i[1]]
		print(dicc)
	else:
		o = list(dicc[i[0]])
		print(dicc)
		print dicc[i[0]]
		print type(o)
		print o.append(i[1])
		lista1=[1]
		print lista1.append(2)
		dicc[i[0]] = o.append(i[1])
		print(dicc)
	pass
"""
"""
def saluda (nombre, apellido):
	print "hola" + nombre + apellido
saluda ('perez', 'juan')

saluda (apellido ='perez', nombre = 'juan')
"""
"""
print "Ingrese el numero a calcular el Factorial" 
num=input()

def factorial (numero):
	valor=numero
	for i in range(1,numero):
		valor*=i
	return [valor] 

valor= factorial(num)
print valor
		
"""

def factorial (numero, *numeros):
	valor=numero
	print numero
	print numeros
	for i in xrange(1,numero):
		valor*=i
	return valor 

valor= factorial(2, 3, 4)
print valor
		
