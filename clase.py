print "hola mundo"
a=3
b=8
c=a+b
print "el resultado es:" + str(c)


iva = 10.
harina = 5
r=(iva*harina)/100
rf=harina+r
print rf
print "iva" + str(r)


a=10
b=10
if a>b:
	print a
else:
	print b
	



suma=1
for i in range(1,101):
	print i

for e in "hola mundo":
	print e

numero = int(input("Digame cuantas palabras tiene la lista: "))

if numero < 1:
    print("Imposible")
else:
    lista = []
    for i in range(numero):
		
        print i
        palabra = raw_input("Digame la palabra " + str(i + 1) + ": ")
        lista += [palabra]
    print "La lista creada es :"  
    print lista


