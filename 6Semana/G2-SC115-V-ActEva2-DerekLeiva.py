#---------Ejercicio#1----------

# for i in range(1,101):
#     print("Numero: ",i)
    
#---------Ejercicio#2----------

# for i in range(51,1,-1):
#     if(i %2==0):
#         if(i==10 or i==40):
#             print("")
#         else:
#             print(i)


#---------Ejercicio#3----------
# nMayor=0
# nMenor=100
# cantPar=0
# cantImp=0

# promedio=0
# for i in range(10):
#     num=int(input("Introduzca numeros: "))
#     if num%2==0:
#         cantPar=cantPar+1
#     else:
#         cantImp=cantImp+1

#     if num > nMayor:
#         nMayor=num
#     if num < nMenor:
#         nMenor=num

#     promedio=promedio+num
#     prom=promedio//10

# print("Cantidad de pares",cantPar,"cantidad de impares",cantImp,
#         "numero mayor",nMayor,"numero menor",nMenor,"Promedio de numeros",prom)

#-------------Ejercicio#4----------

# letrasVo=0
# letrasCons=0
# cant=int(input("Ingrese cantidad de letras a utilizar: "))
# for i in range(cant):
#     letras=input("Digite las letras: ")
#     if letras =="a" or letras=="e" or letras=="i" or letras=="o" or letras=="u" :
#         letrasVo=letrasVo+1
#     else:
#         letrasCons=letrasCons+1

# print("Hay",letrasVo,"vocales, y",letrasCons,"consonantes")


#--------------Ejercicio#5 Presentacion-------------------

# num=int(input("Digite un numero a analizar: "))
# if num%2!=0:
#     print("Es primo")
# else:
#     print("No es primo")
#--------------Ejercicio#9 Presentacion-------------------

# mayorE=0
# menorE=0
# for i in range(20,-1,-1):
#     edad=int(input("Ingrese su edad: "))
#     if edad <=18:
#         mayorE=mayorE+1
#     else:
#         menorE=menorE+1
#     if(i==0):
#         print("Entradas agotadas")    
# print("Las entradas fueron comprados por",mayorE,"mayores de edad y",menorE,"menores de edad")
