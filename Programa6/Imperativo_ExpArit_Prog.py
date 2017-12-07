#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#	Materia: Lenguajes de Programación
#	Equipo:	* Aguilar Enriquez, Paul Sebastian - 415028130
#			* Badillo Lora, Raúl - 415033808
#			* Cabrera López, Oscar Emilio - 312333261
#	Programa:
#	(B) Desarrollar la función evaluar. La función consume (la representación de)
#	una expresión numérica y calcula su valor.

#	(C) Cuando se evalúan expresiones con variables, se sustituyen variables con
#	valores.
#	Desarrollar la función subst. Consume (la representación de) una expresión
#	Racket, (la representación de) una variable (v) y un número (n). Produce una
#	expresión estructuralmente equivalente en la cual todas las ocurrencias de v
#	son sustituidas por n.

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

# Funcion que sustituye una literal por su valor numerico
def subst(expresion):
	"""
	funcion subst

	Sustituye el valor numerico de las literales en una expresion

	args:
	expresion: Expresion a evaluar

	returns:
	nExpresion: Retorna la nueva expresion con los valores numericos sustituidos

	"""
	# Separamos datos
	data = expresion.split(',')
	E = data[0]
	if len(data) > 1:
		L = data[1].split()
	else:
		L = []

	# Revisamos si puede existir la posible ausencia de valores en la relacion de
	# literales y valores numericos
	if not (len(L)%2 == 0):
		return "Incomplete " + expresion

	nE = ""

	# Sustituimos valores numericos en las literales
	x = 0
	while x < len(L):
		y = 0
		while y < len(E):
			if E[y] == L[x]:
				nE += L[x+1]
			else:
				nE += E[y]
			y+=1
		x+=2
		E = nE
		nE = ""

	# Verificamos si aun quedan literales en la la expresion
	for c in E:
		if c.isalpha() and not(c == "V" or c == "F"):
			return "NaN " + expresion

	return E

# Funcion que evalua una expresion bien formada
def evaluar(expresion):
	"""
	funcion evaluar

	Evalua una expresión bien formada

	args:
	expresion: Expresion a evaluar

	returns:
	N: Retorna True si la expresion coincide con el valor dado, False en caso contrario

	"""
	if expresion[0] == "N" or expresion[0] == "I":
		return "No se puede evaluar "

	data = expresion.split()
	dicV = {'V':'True', 'F':'False'}
	dicOBin = {'+':'+', '-':'-', '*':'*', '/':'/', '^':'**', '=':'==', '<=':'<=', '&':'and', '|':'or'}
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
				va = eval(str(N.pop()) + " " + dicOBin[op] + " " + str(va))
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
	"""
	funcion tdd

	Ejecuta una funcion que evalua una expresion bien formada, imprimiendo a la
		expresion misma, el resultado esperado, el resultado obtenido y
		Verdadero o Falso si es que ambos resultados coinciden o difieren.

	args:
	function: Función a ejecutar
	parameters: Expresion a evaluar
	results: Resultados esperados

	returns:
	parameters: expresion bien formada
	result: resultado esperado de evaluar la expresion
	resultF: resultado de evaluar la expresion
	Verifica si el resultado esperado y el obtenido son iguales

	"""
	resultF = function(parameters)
	return parameters, results, resultF, resultF == results,

# Main
print(evaluar(subst('( ( x + y ) - z ) , x 3 y 5 z 1')))

print(tdd(evaluar, subst('( x + y ) , x 3 y 5'), [8.0]))
print(tdd(evaluar, subst('( x + y ) , x 3 y 5 z'), [8.0]))
print(tdd(evaluar, subst('( x + z ) , x 3 y 5'), [8.0]))

print(tdd(evaluar, subst('( x + z ) , x 3 z 5'), [8.0]))
print(tdd(evaluar, subst('( x + z ) , x 3 z 5'), [5.0]))

print(tdd(evaluar, subst('( x - z ) , x 3 z 5'), [-2.0]))
print(tdd(evaluar, subst('( x - z ) , x 3 z 5'), [5.0]))

print(tdd(evaluar, subst('( x * z ) , x 3 z 5'), [5.0]))
print(tdd(evaluar, subst('( x * z ) , x 3 z 5'), [15.0]))

print(tdd(evaluar, '( 5 / 5 )', [1.0]))
print(tdd(evaluar, '( 5 / 5 )', [5.0]))

print(tdd(evaluar, subst('( ¬ V ),V 0'), [True]))
print(tdd(evaluar, subst('( ¬ V )'), [True]))
print(tdd(evaluar, subst('( ¬ x )'), [True]))

print(tdd(evaluar, '( ¬ V )', [True]))
print(tdd(evaluar, '( ¬ F )', [True]))
print(tdd(evaluar, '( V | F )', [True]))
print(tdd(evaluar, '( V & F )', [False]))

print(tdd(evaluar, '( V = ( 3 <= 5 ) )', [True]))
print(tdd(evaluar, '( V = ( 3 <= 5 ) )', [False]))

print(tdd(evaluar, '( F = ( 3 <= 5 ) )', [False]))
print(tdd(evaluar, '( F = ( 3 <= 5 ) )', [True]))

print(tdd(evaluar, '( ¬ ( ( 5 <= 1 ) ) = ( 3 <= 5 ) )', [True]))
print(tdd(evaluar, '( ¬ ( ( 5 <= 1 ) ) = ( 3 <= 5 ) )', [False]))

print(tdd(evaluar, '( ¬ ( ¬ ( ( 5 * 3 ) <= ( 7 ) ) )', [False]))
print(tdd(evaluar, '( ¬ ( ¬ ( ( 5 * 3 ) <= ( 7 ) ) )', [True]))
