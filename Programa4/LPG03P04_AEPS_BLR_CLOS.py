#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	Materia: Lenguajes de Programación
#	Equipo:	* Aguilar Enriquez, Paul Sebastian - 415028130
#			* Badillo Lora, Raúl - 415033808
#			* Cabrera López, Oscar Emilio - 312333261
#	Programa:	Desarrollar un programa que dado un valor en base diez lo convierta a punto flotante binario

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

# Funcion que convierte el valor decimal a punto flotante binario
def dec_to_binfloat(number):
    """
	funcion dec_to_binfloat

	Recive un numero decimal de punto flotante y lo convierte a su valor en binario.

	args:
	number: numero decimal a convertir

	returns:
	strnum: valor convertido a binario

	"""
    strfrac = ''    # Parte fraccionaria
    strnum = ''     # Parte entera
    strsig = ''     # Bit de signo

    # Verificamos el signo
    if number < 0:
        strsig = '1'
        number = -1 * number
    else:
        strsig = '0'

    strnum = bin(int(number // 1))[2:] + '.'    # Convertimos la parte entera a binario
    number = number % 1  # Removemos la parte entera del numero

    # Convertimos la parte decimal a binario
    while number != 0:
        number = number * 2
        strfrac += str(int(number // 1))
        number = number % 1
    strnum += strfrac   # Conversion binaria del decimal, incluye el punto

    # Normalizamos
    exp = strnum.index('.') - 1 # Buscamos el indice del . como referencia
    strnum = ''.join(strnum.split('.')) # Retiramos el punto
    exp -= strnum.index('1')    # Obtenemos el exponente en base 2

    # Obtenemos la mantisa
    if exp < 0:
        strnum = strnum[(-1*exp)+1:]
    else:
        strnum = strnum[1:]
    exp += 127  # Obtenemos el exponente en decimal
    strnum = strsig + bin(exp)[2:].rjust(8, '0') + strnum.ljust(23, '0')    # Unimos todos los elementos del valor en binario
    return strnum

# Main
def main():
	"""
	funcion main
	"""
    num = input("Ingrese el número a convertir: ")
    num = eval(num)
    print(dec_to_binfloat(num))

if __name__ == '__main__':  # si se ejecuta como script
	import sys
	try:
		sys.exit(main())
	except (KeyboardInterrupt, SystemExit):  # No lances un error ante la
		sys.exit(0) # finalizacion del programa
