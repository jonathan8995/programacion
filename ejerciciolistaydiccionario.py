lista=[7,9,2,10,4]
print lista[0:1]
iterador=-1
for i in lista:
	print lista [iterador]
	iterador=iterador-1

nombre='name'
diccionario={}
print diccionario
diccionario['nombre2']='luis'
print diccionario
diccionario['nombre']='paola'
print diccionario

for i in diccionario:
	print diccionario[i]
nombre=['jose','kevin','ibrahim','brayan']
dato=0
for i in nombre:
	diccionario['nombre'+str(dato)]=i
	dato=dato+1	
print diccionario	

def Suma(num1,num2):
	total=num1+num2
	return total 
print Suma(1,4)	
