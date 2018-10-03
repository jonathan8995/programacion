lista=[7,9,2,10,4]
iterador=0
for i in lista:
	print lista [iterador]
	iterador=iterador-1

diccionario={'animal1':'oso','animal2':'jirafa','animal3':'leon'}
print diccionario
print diccionario.keys()
print diccionario.values()
diccionario['animal4']='vaca'
print diccionario
diccionario['animal1']='perro'
for i in diccionario:
	print diccionario[i]
