#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	Materia: Lenguajes de Programación
#	Equipo:	* Aguilar Enriquez, Paul Sebastian - 415028130
#			* Badillo Lora, Raúl - 415033808
#			* Cabrera López, Oscar Emilio - 312333261
#	Programa:	Desarrollar un programa que evalúe expresiones booleanas bien
#	formadas en el lenguaje definido (notación infija) utilizando el algoritmo propuesto.

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

from math import *

# Funcion que convierte el valor decimal a punto flotante binario
def sy(expresion):
	"""
	funcion sy

	Evalua una expresión bien formada

	args:
	expresion: Expresion a evaluar

	returns:
	N: Retorna True si la expresion coincide con el valor dado, False en caso contrario

	"""

	data = expresion.split()
	dicV = {'V':'True', 'F':'False'}
	dicOBin = {'+':'+', '*':'*', '/':'/', '^':'**', '=':'==', '<=':'<=', '&':'and', '|':'or'}
	dicOUna = {'raiz':'sqrt', 'sen':'sin', '¬':'not'}
	S, N = [], []
	for e in data:
		if e == '(':
			pass
		elif (e in dicOBin) or (e in dicOUna):
			S.append(e)
		elif e == ')':
			op, va = S.pop(), N.pop()
			if op in dicOBin:
				va = eval(str(N.pop()) + dicOBin[op] + str(va))
			else:
				va = eval(dicOUna[op] + '(' + str(va) + ')')
			N.append(va)
		else:
			if e in dicV:
				e = dicV[e]
			else:
				e = float(e)
			N.append(e)
	return N


def tdd(function, parameters, results):
	return function(parameters) == results

# Main
print(tdd(sy, '( 3 * 5 )', [15.0]))
print(tdd(sy, '( 3 * 5 )', [5.0]))
print(tdd(sy, '( V = ( 3 <= 5 ) )', [False]))
print(tdd(sy, '( V = ( 3 <= 5 ) )', [True]))
print(tdd(sy, '( ¬ ( ( 5 <= 1 ) ) = ( 3 <= 5 ) )', [False]))
print(tdd(sy, '( ¬ ( ( 5 <= 1 ) ) = ( 3 <= 5 ) )', [True]))
print(tdd(sy, '( ¬ ( ¬ ( ( 5 * 3 ) <= ( 7 ) ) )', [False]))
print(tdd(sy, '( ¬ ( ¬ ( ( 5 * 3 ) <= ( 7 ) ) )', [True]))
