# coding: utf-8
numero1 = input("Introduce el primer número :")
numero2 = input("Introduce segundo número :")

if (numero1 > numero2):
	print "numero1 es el mayor"
else:
	if (numero2 > numero1):
		print "numero2 es el mayor"
	else:
		if (numero1 == numero2):
			print "numero1 es igual que numero2"
