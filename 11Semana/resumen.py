#importa funcionalidades relacionadas al sistema operativos

import os 

#configura archivo--------------------
# file=open("miarchivo.txt","w") #"W" crear archivo para escritura 

# #para escribir en un archivos, usar comando "file.write"---------------
# file.write("Hola mundo\n")
# file.write("escrito desde vs")
# file.close()


#permite escribir en el arhivo sin borrar-------------------------
# file=open("miarchivo.txt","a") #"a" crear archivo para escritura
# #escribir
# file.write("Hola mundo\n")
# file.write("escrito desde vs\n")
# file.close()

#-------------------------------------------------SEGUNDO EJEMPLO-------------------------------------------------------------

# file=open("nombre.txt","r") #"r" leer para lectura
# contenido=file.read() #cargar todo el contenido del archivo en una variable
# print(contenido)

# #pasando los datos de una variable a un arreglo
# file=open("nombre.txt","r") #"r" leer para lectura
# contenido=file.read() #cargar todo el contenido del archivo en una variable
# convec=contenido.split("\n") #separar el contenido en un arreglo
# contar=0

# for i in range (len(convec)):
#     if convec[i]=="Derek":
#         contar=contar+1

# print(contar)
# file.close()


#-------------------------------------------------Tercer EJEMPLO-------------------------------------------------------------

#crear archivo
# file=open("datosCurso.txt","a") #"a" escribir en el archivo sin borrar
# print("Archivo listo para ser usado")
# file.close()

# #leer datos de una persona
# nom=input("Ingrese su nombre: ")
# telefono=input("Ingrese su telefono: ")
# file=open("datosCurso.txt","a") #"a" escribir sin borrar
# file.write(nom+"\n"+telefono+"\n") 
# print("Datos guardados")
# file.close()

# #imprimir info de un archivo

# file=open("datosCurso.txt","r") #"r" leer para lectura
# contenido=file.read()
# print(contenido)
# file.close()

#-------------------------------------------------CUARTA EJEMPLO-------------------------------------------------------------

#crear archivo
# file=open("datosCurso.txt","a") #"W" crear archivo para escritura
# print("Archivo listo para ser usado")
# file.close()

# #leer datos de una persona
# for i in range(1,11):
#     nom=input("Ingrese su nombre: ")
#     telefono=input("Ingrese su telefono: ")
#     file=open("datosCurso.txt","a") #"a" escribir sin borrar
#     file.write(nom+"\n"+telefono+"\n") 
#     print("Datos guardados")
#     file.close()

# # nom=input("Ingrese su nombre: ")
# # telefono=input("Ingrese su telefono: ")
# # file=open("datosCurso.txt","a") #"a" escribir sin borrar
# # file.write(nom+"\n"+telefono+"\n") 
# # print("Datos guardados")
# # file.close()

# #imprimir info de un archivo

# file=open("datosCurso.txt","r") #"r" leer para lectura
# contenido=file.read()
# print(contenido)
# file.close()

#-------------------------------------------------QUINTO EJEMPLO-------------------------------------------------------------

# def leerArchivo():
#     file=open("datosCurso.csv","a") #"W" crear archivo para escritura
#     print("Archivo listo para ser usado")
#     file.close()

# def meterPersonas():
#     for i in range(1,11):
#         nom=input("Ingrese su nombre: ")
#         telefono=input("Ingrese su telefono: ")
#         file=open("datosCurso.csv","a") #"a" escribir sin borrar
#         file.write(nom+"\n"+telefono+"\n") 
#         print("Datos guardados")
#         file.close()

# def imprimirArchivo():
#     file=open("datosCurso.csv","r") #"r" leer para lectura
#     contenido=file.read()
#     print(contenido)
#     file.close()

# num=""

# while num!=0:
#     numa=int(input("Ingrese un numero: "))
#     if numa==1:
#         leerArchivo()
#     elif numa==2:
#         meterPersonas()
#     elif numa==3:
#         imprimirArchivo()

