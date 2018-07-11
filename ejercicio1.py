
print 'Digame cuantas palabras desea ingresar'
num = int(raw_input())
lista=[]
for i in range(num):
	pala= str(raw_input('Ingrese la palabra '+ str(i+1) + ': '))	
	lista.append(pala)

print lista

