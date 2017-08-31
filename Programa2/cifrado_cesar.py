#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Emilio Cabrera, Sebastian Aguilar, Raúcll Badillo
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


"""cifrado_cesar

Este programa usa una variante del cifrado césar para encriptar una cadena de
texto o un archivo de texto simple.

El proceso consiste en desplazar una cantidad n de caracteres cada letra,
de forma intercalada hacia la izquierda y la derecha cada vez. Por esto,
para desencriptar un texto bastará que se ejecute de nuevo el programa con la
misma cantidad n de lugares a desplazar pero iniciando el desplazamiento en la
dirección contraria.

Example:
    Encriptar una cadena desde la entrada estandar
        $ ./cifrado_cesar.py
    Encriptar una cadena desde la entrada estandar iniciando el
        desplazamiento por la izquierda
        $ ./cifrado_cesar.py -l
    Encriptar una cadena pasada como argumento
        $ ./cifrado_cesar.py -t "cadena a encriptar"
    Encriptar una cadena desplazando cada caracter n lugares
        $ ./cifrado_cesar.py -n 5
    Encriptar un archivo de texto
        $ ./cifrado_cesar.py -f /ruta/del/archivo.txt
    Para más opciones
        $ ./cifrado_cesar.py -h
"""


def command_parse():
    """command_parse

        Procesa los argumentos que se envian al programa cuando se corre como
        script desde la linea de comandos.

        Para más información ver:
        https://docs.python.org/3/library/argparse.html

        Returns:
            obj, argparse.Namespace: objeto cuyos atributos contienen los
                valores de cada argumento.
    """
    argparser = argparse.ArgumentParser(description="Programa de codificación "
                                                    "césar para texto plano")
    argparser.add_argument("-f", "--file", type=argparse.FileType('r'),
                           help="Archivo de texto plano para codificar")
    argparser.add_argument("-o", "--output", type=argparse.FileType('w+'),
                           help="Archivo de salida")
    argparser.add_argument("-n", "--num",  type=int, default=5,
                           help="Numero de caracteres a recorrer (default: 5)")
    argparser.add_argument("-t", "--text",  help="Cadena de caracteres para "
                                                 "codificar")
    argparser.add_argument("-l", "--lshift", action='store_true',
                           help="El primer corrimiento será a la izquierda")
    return argparser.parse_args()


def cesar(text, num, rshift):
    """cesar

        Recibe una lista de cadenas y para cada una desplaza sus caractares de
        forma intercalada a la izquierda y la derecha.
        La funcion trabaja solo con los caracteres imprimibles del codigo ascii
        y puede devolver valores inesperados para cualquier otro conjunto de
        caracteres, incluyendo ascii extendido.

        Args:
            text (list): lista de cadenas a encriptar
            num (int): numero de lugares a desplazar cada letra.
            rshift (bool): indica si el desplazamiento inicia a la derecha
                (True) o por la izquierda (False).

        Returns:
            list: Lista con las cadenas encriptadas.
    """
    shift = num if rshift else -num
    codedtext = []
    for line in text:
        codedline = ""
        line = line.lower()
        for char in line:
            newchar = ord(char) + shift
            if newchar > 126:
                newchar = 32 + ord(char) - 127 + shift
            elif newchar < 32:
                newchar = 127 + ord(char) - 32 + shift
            codedline += chr(newchar)
            shift = -shift
        codedtext.append(codedline)
    return codedtext


def main():
    """main

    Funcion principal del programa, determina que argumentos fueron pasados,
        llama a la funcion cesar de forma adecuada y presenta los resultados
        en un archivo o a la salida estándar (stdout).

    Returns:
        int: Cero al finalizar el programa
    """
    args = command_parse()
    text = []
    shift = True if not args.lshift else False
    if args.file:
        for line in args.file:
            line = line.strip('\n')
            if not line:
                continue
            text.append(line)
    elif args.text:
        text.append(args.text)
    else:
        text.append(input("Escribe el texto que quieras codificar: "))
    if args.output:
        args.output.writelines('\n'.join(cesar(text, args.num, shift)))
    else:
        for line in cesar(text, args.num, shift):
            print(line)
    return 0


if __name__ == '__main__':  # si se ejecuta como script
    import sys
    import argparse
    try:
        sys.exit(main())
    except (KeyboardInterrupt, SystemExit):  # No lances un error ante la
        sys.exit(0)                          # finalizacion del programa
