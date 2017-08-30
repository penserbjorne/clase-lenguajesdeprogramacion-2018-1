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

from collections import deque

chars = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
specialchars = ('ā', 'á', 'ǎ', 'à', 'ē', 'é', 'ě', 'è', 'ī', 'í', 'ǐ', 'ì',
                'ō', 'ó', 'ǒ', 'ò', 'ū', 'ú', 'ǔ', 'ù', 'ü', 'ǘ', 'ǚ', 'ǜ')
specialdict = {'ā': 'a', 'á': 'a', 'ǎ': 'a', 'à': 'a', 'ē': 'e', 'é': 'e',
               'ě': 'e', 'è': 'e', 'ī': 'i', 'í': 'i', 'ǐ': 'i', 'ì': 'i',
               'ō': 'o', 'ó': 'o', 'ǒ': 'o', 'ò': 'o', 'ū': 'u', 'ú': 'u',
               'ǔ': 'u', 'ù': 'u', 'ü': 'u', 'ǘ': 'u', 'ǚ': 'u', 'ǜ': 'u'}


def command_parse():
    argparser = argparse.ArgumentParser(description="Programa de codificación "
                                                    "césar para texto plano")
    argparser.add_argument("-f", "--file", type=argparse.FileType('r'),
                           help="Archivo de texto plano para codificar")
    argparser.add_argument("-n", "--num",  type=int, default=5,
                           help="Numero de caracteres a recorrer (default: 5)")
    argparser.add_argument("-t", "--text",  help="Cadena de caracteres para "
                                                 "codificar")
    argparser.add_argument("-s", "--shift", type=bool, default=True,
                           choices={'der': True, 'izq': False},
                           help="En que dirección será el primer corrimiento")
    return argparser.parse_args()


def cesar(text, num, shift):
    rshiftchars = chars.copy()
    lshiftchars = chars.copy()
    rshiftchars.rotate(num)
    lshiftchars.rotate(-num)
    flag = shift
    codedline = ""
    codedtext = []
    for line in text:
        line = line.lower()
        for char in line:
            if char in specialchars:
                char = specialdict[char]
            if char in chars:
                if flag:
                    codedline += rshiftchars[chars.index(char)]
                else:
                    codedline += lshiftchars[chars.index(char)]
            else:
                codedline += char
            flag = not flag
        codedtext.append(codedline)
    return codedtext


def main():
    args = command_parse()
    text = []

    if args.file:
        for line in args.file:
            text.append(line)
    elif args.text:
        text.append(args.text)
    else:
        text.append(input("Escribe el texto que quieras codificar: "))
    for line in cesar(text, args.num, args.shift):
        print(line)


if __name__ == '__main__':
    import sys
    import argparse
    sys.exit(main())
