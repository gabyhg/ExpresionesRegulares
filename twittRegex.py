#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  twittRegex.py
#
#  The MIT License (MIT)
#
#  Copyright (c) 2016
#    Emilio Cabrera <emilio1625@gmail.com>
#    Gabriela Hernández García <gabyhernandezgarcia3@gmail.com>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.



def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Archivo html de twitter.com del que se extraerán los usuarios")
    parser.add_argument("-o", "--output", help="Archivo donde se guardarán los usuarios recuperados, si se omite se usará el archivo usuarios.txt (si no existe)")
    args = parser.parse_args()
    if args.file:
        with open(args.file, "r") as archivo:
            usuarios = getUsuarios(archivo)
            usuarios = list(sorted(set(usuarios)))
        if args.output:
            with open(args.output, "w") as salida:
                for n in range(0,len(usuarios)):
                    salida.write("@" + usuarios[n] + "\n")
        else:
            with open("usuarios.txt", "w") as salida:
                for n in range(0,len(usuarios)):
                    salida.write("@" + usuarios[n] + "\n")
    else:
        print "Debes dar un archivo para trabajar"
        print "Prueba 'twittRegex -h' para más información"
    return 0

def getUsuarios(archivo):
    contenido = archivo.read()
    usuarios = []
    objRegex = re.findall(r"@(\w+)", contenido)
    for n in range(0, len(objRegex)):
        usuarios.append(objRegex[n])
    objRegex = re.findall(r"@<\/s><(\w+)>(.*?)<\/(\1)>", contenido)
    for n in range(0, len(objRegex)):
        a = objRegex[n][1]
        if (a != ''):
            usuarios.append(a)
    objRegex = re.findall(r"@<(.*) (.*)>(.*?)<\/(\1)>", archivo.read())
    for n in range(0, len(objRegex)):
        a = objRegex[n][2]
        if (a != ''):
            usuarios.append(a)
    return usuarios

if __name__ == '__main__':
    import sys
    import re
    import argparse
    sys.exit(main(sys.argv))