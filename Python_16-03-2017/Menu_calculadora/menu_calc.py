# coding: utf-8

print "S.- Salir"
print "1.- Sumar"
print "2.- Restar"
print "3.- Multiplicar"
print "4.- Dividir"

opcion = input("¿Que desea hacer el amo? :")
numero1 = input("Introduce el primer numero :")
numero2 = input("Introduce el segundo numero :")
		
if opcion == 1 :
	sumar = numero1 + numero2
	print sumar

if opcion == 2 :
	restar = numero1 - numero2
	print restar
	
if opcion == 3 :
	multiplicar = numero1 * numero2
	print multiplicar
	
if opcion == 4 :
	dividir = numero1 / numero2	
	print dividir

if opcion == "s" or opcion == "S":
	print "Adios"
