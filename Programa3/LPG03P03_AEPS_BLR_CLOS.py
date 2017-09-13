#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	Materia: Lenguajes de Programación
#	Equipo:	* Aguilar Enriquez, Paul Sebastian - 415028130
#			* Badillo Lora, Raúl - 415033808
#			* Cabrera López, Oscar Emilio - 312333261
#	Programa:	Desarrollar un programa que obtenga la representación C_1 y C_2
#				de un número entero que se encuentra en base 10 y viceversa.

# Copyright (c) 2017
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def binario(num):
	"""
	funcion binario

	Recive un numero decimal y lo convierte a su valor absoluto en binario al reves.
	Divide sucesivamente al numero entre dos y guarda el residuo en una lista, este es el numero
	binario.

	args:
	num: numero decimal a convertir

	returns:
	bi(list): lista con digitos binarios

	"""
	bi = []
	num = abs(int(num))
	while num >0:
		res = num % 2
		bi.append(res)

		num = num //2

	return bi


def comp1(numb):
	"""
	funcion comp1
	convierte a un numero decimal a complemento a1
	manda a llamar a la funcion binario para obtener el valor absoluto en
	binario, si es que el numero es negativo invierte cada uno de los digitos
	del numero y le anexa el bit de signo correspondiente y lo invierte para ponerlo en el orden correcto
	si es positivo solamente le anexa el bit de signo y lo invierte

	args:
	num: numero decimal a convertir

	returns:
	c11(list): lista con digitos en complemento a 1

	"""

	bi= binario(numb)
	c11 = []
	if int(numb) < 0:
		for x in bi:
			c11.append(int( not x))

		c11.append(1)
		c11.reverse()
	else:
		c11 = bi
		c11.append(0)
		c11.reverse()
	return  c11


def comp2(numb):
	"""
	funcion comp2
	convierte a un numero decimal a complemento a 2
	manda a llamar a la funcion comp1 para obtener el valor  en
	comp1.
	Recorre los digitos empezando per el bit menos significativo obteniendo
	su negado hasta encontrarse con un 0, esto es equivalente a sumarle 1

	args:
	num: numero decimal a convertir

	returns:
	c22(list): lista con digitos en complemento a 2

	"""
	c1 = comp1(numb)
	c22 = []
	if int(numb) < 0:
		lsb = 0
		while lsb == 0:
			lsb = int(not c1.pop())
			c22.append(lsb)
		c1.reverse()
		c22 = c22 + c1
		c22.reverse()
	else:
		c22 = c1
	return c22



def dec(list, c1):
	"""
	funcion dec
	convierte a una lista de digitos en binario a un numero decimal
	manda a llamar a la funcion comp1 para obtener el valor  en
	comp1.
	Recorre los digitos empezando per el bit menos significativo obteniendo
	su negado hasta encontrarse con un 0, esto es equivalente a sumarle 1

		args:
	num: numero decimal a convertir

	returns:
	c22(list): lista con digitos en complemento a 2

	"""

	potencia = 0
	decnumb = 0
	while len(list)>1:
		decnumb += list.pop() * 2 ** potencia
		potencia += 1
	print (list)
	if list[0] == 1:

		decnumb = (decnumb * -1)
		if c1 is True:
			decnumb = decnumb - 1

	return decnumb


def decimal(inte, c1):
	"""
	esta funcion convierte a una string en una lista de digitos y se la
	pasa a la funcion dec
	"""

	vector = list(str(inte))
	vec = []
	for n in range(len(vector)):
		vector[n] = int(vector[n])

	return dec(vector,c1)


def stringer(list):
	"""
	esta funcion convierte una lista de digitos en una cadena
	"""
	string = ""
	for x in list:
		string = string + str(x)
	return string


def main():
	"""
	funcion main con menu de opciones
	"""

	while True:
		seleccion = input("selecciona:\n\t1) c1 a decimal\n\t2) c2 a decimal\n\t3) decimal a c1\n\t4) decimal a c2\n\t5) salir\nOpcion: ")
		if int(seleccion) == 1:
			numb = input("Introduce el numero en c_1: ")
			print (decimal(numb,True))
		elif int(seleccion) == 2:
			numb = input("Introduce el numero en c_2: ")
			print (decimal(numb,False))
		elif int(seleccion) == 3:
			numb = input("Introduce el numero en decimal: ")
			print (stringer(comp1(numb)))
		elif int(seleccion) == 4:
			numb = input("Introduce el numero en decimal: ")
			print (stringer(comp2(numb)))
		elif int(seleccion) == 5:
			print ("Saliendo.")
			exit();
			break

if __name__ == '__main__':  # si se ejecuta como script
	import sys
	try:
		sys.exit(main())
	except (KeyboardInterrupt, SystemExit):  # No lances un error ante la
		sys.exit(0) # finalizacion del programa
