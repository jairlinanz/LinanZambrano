import os
import csv
from operator import delitem
import operator

print("\nEvidencia_taller_3 y solucion: \n")

contenidocarpeta= os.listdir('C:/Users/Personal/Desktop/LinanZambrano/Files')

ruta='C:/Users/Personal/Desktop/LinanZambrano/Files'

print("\n1. lista de archivos de la carpeta Desktop/LinanZambrano/Files: ",contenidocarpeta)
print("\n Nombres, extenciones y ruta de los archivos contenidos en la carpeta: \n")

for archivo in contenidocarpeta:
    nombre, extension = os.path.splitext(archivo)
    print("El nombre del archivo es '{}' y la extension es '{}', su ruta es: {}".format(nombre, extension, ruta))

print("\n 2. Este es el contenido del archivo Usuarios.csv: \n")


with open('C:/Users/Personal/Desktop/LinanZambrano/Files/Usuarios.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("\n 3. Esta es la informacion solicitada, del archivo Usuarios.csv, con las columnas solicitadas: \n")

with open('C:/Users/Personal/Desktop/LinanZambrano/Files/Usuarios.csv') as f:
    reader = csv.reader(f, delimiter=',')
    cantidad_columnas= len('Usuarios.csv')-1
    for row in reader:
        print("{0}, {1}, {2}, {3}".format(row[1], row[2], row[4], row[10]), "Cantidad de columnas por usuario: ", cantidad_columnas)
