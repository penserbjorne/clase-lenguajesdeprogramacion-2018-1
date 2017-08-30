#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Emilio Cabrera
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


def command_parse():
    argparser = argparse.ArgumentParser(description="Programa de codificación "
                                                    "césar para texto plano")
    argparser.add_argument("-f", "--file", type=argparse.FileType('r'),
                           help="Archivo de texto plano para codificar")
    argparser.add_argument("-n", "--num",  type=int, default=5,
                           help="Numero de caracteres a recorrer (default: 5)")
    argparser.add_argument("-t", "--text",  help="Cadena de caracteres para "
                                                 "codificar")
    argparser.add_argument("-l", "--lshift", action='store_true',
                           help="El primer corrimiento será a la izquierda")
    return argparser.parse_args()


def cesar(text, num, rshift):
    shift = num if rshift else -num
    codedline = ""
    codedtext = []
    for line in text:
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
    args = command_parse()
    text = []
    shift = True if not args.lshift else False
    if args.file:
        for line in args.file:
            text.append(line)
    elif args.text:
        text.append(args.text)
    else:
        text.append(input("Escribe el texto que quieras codificar: "))
    for line in cesar(text, args.num, shift):
        print(line)


if __name__ == '__main__':
    import sys
    import argparse
    sys.exit(main())
