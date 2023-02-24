#-----------------Ejericios #1----------
# nombres=[]
# for i in range(0,5):
#     nombre=input("Digite un nombre: ")
#     nombres.append(nombre)
# print("Nombres digitados\n",nombres)
# preg=int(input("Desea cambiar algun nombre? 1=SI || 2=NO: "))
# if preg== 1:
#     ind=int(input("Digite la posicion del nombre que desea cambiar: "))
#     nombre=input("Digite el nuevo nombre: ")
#     nombres[ind]=nombre
#     print(nombres)
# else:
#     print("chao")

#----------------Ejericios #2----------
# sNotas=0
# notas=[]
# materia=input("Materia: ")
# nombre=input("Nombre: ")
# for i in range(5):
#     nota=int(input("Nota: "))
#     notas.append(nota)
#     sNotas=sNotas+nota
# prom=sNotas/5
# print("Estudiante",nombre,"\nEl promedio final de la materia",materia,"es",prom,"\nEste es el glosaria de sus notas",notas)

#----------------Ejericios #3-------------
# numeros=[]
# for i in range(1,11):
#     num=int(i)
#     numeros.append(num)

# suma=numeros[1-1]+numeros[5-1]+numeros[10-1]
# resta=numeros[2-1]+numeros[8-1]
# multi=numeros[9-1]+numeros[3-1]
# divi=numeros[4-1]+numeros[7-1]
# print(numeros,"\nLa suma es",suma,"\nLa resta es",resta,"\nLa divi es",divi,"\nLa multi es",multi,)

#----------------Ejericios #4-----------------
# arregloA=[]
# arregloB=[]
# arregloC=[]
# for i in range(1,6):
#     num=int(input("numero para array A: "))
#     arregloA.append(num)
# print("------")
# for i in range(1,6):
#     num=int(input("numero para array B: "))
#     arregloB.append(num)
# for i in range(1,6):
#     suma=arregloA[i-1]+arregloB[i-1]
#     arregloC.append(suma)
# print("ArregloA:",arregloA,"\nArregloB:",arregloB,"\nArregloC:",arregloC)

#-------------------Ejercicio #5-------------
numeros=[]
# f=int(input("Numeros de filas: "))
# c=int(input("Numeros de columnas: "))

for i in range(1):
    numeros.append([0]*2) 

# for i in range(c):
#     for j in range(f):
#         num=int(input("Ingrese el numero:"))
#         numeros[i][j]=num
print(numeros)
# for i in range(c):
#     for j in range(f):
#         if numeros[i][j]<0:
#             numeros[i][j]=0

# print(numeros)                




