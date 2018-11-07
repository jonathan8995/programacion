print "Porfavor indiquenos la cantidad de palabras que quieres asignar"
palabras = input()
print "Digame cuantas palabras tiene la lista =" + str(palabras)
lista = []
for i in range (palabras):
    palabras2= raw_input ("Digame la palabra " + str(i+1) + " ")
    lista.append(palabras2)

print "lista =" , lista







