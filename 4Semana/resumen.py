#---------------------------------IF SIMPLE----------------------------------

# edad=int(input("Introduzca su edad: "))
# if edad >= 18:
#     print("Bienvenido")

#------EJEMPLO----------

# precio=int(input("Digite el precio: "))
# unidades=int(input("Digite la cantidad de unidades: "))
# calc=precio*unidades

# if unidades >= 12:
#     precio=precio-(precio*0.12)

# print("El precio a pagar es",calc)

#------EJEMPLO #2----------

# sal=int(input("Digite un salario a calcular: "))
# if sal <1000:
#     sal=sal+(sal*0.15)

# print("El salario es de $",sal)

#---------------------------------IF Doble----------------------------------

# edad=int(input("Introduzca su edad: "))
# if edad >= 18:
#     print("Bienvenido")
# else:
#     print("Usted es menor de edad")
    
#-------Ejemplo #1-------

# nota=int(input("Digite la nota: "))

# if nota >= 70:
#     print("El estudiante aprobo")
# else:
#     print("El estudiante reprobo")

#-----Ejemplo #2--------

# sal=int(input("Digite un salario a calcular: "))
# if sal >1000:
#     sal=sal+(sal*0.15)
# else:
#     sal=sal+(sal*0.20)
    
# print("El nuevo salario es de $",sal)

#---------------------------------IF Anidado----------------------------------

# num=int(input("Digite un numero: "))

# if num >= 1000:
#     print ("Este numero es de mas de 3 cifras")
# else:
#     if num >= 100:
#         print ("El numero es de 2 cifras")
#     else:
#         print ("El numero es 1 cifra ")

#-----Ejemplo #1--------
# sal=int(input("Digite un salario: "))
# cat=int(input("Digite una categoria: "))

# if cat == 1:
#     sal=sal+(sal*0.10)
#     print("El nuevo salario es:",sal)
# elif cat == 2:
#     sal = sal+(sal*0.12)
#     print("El nuevo salario es:",sal)
# elif cat == 3:
#     sal = sal+(sal*0.15)
#     print("El nuevo salario es:",sal)
# elif cat == 4:
#     sal = sal+(sal*0.20)
#     print("El nuevo salario es:",sal)
# else:
#     print("No digito ninguna categoria!")
#     print("El salario sigue siendo:",sal)
    
    
# if cat == 1:
#     sal = sal+(sal*0.10)
#     print("El nuevo salario es:",sal)
# else:
#     if cat == 2:
#         sal = sal+(sal*0.12)
#         print("El nuevo salario es:",sal)
#     else:
#         if cat == 3:
#             sal = sal+(sal*0.15)
#             print("El nuevo salario es:",sal)
#         else:
#             if cat == 4:
#                 sal = sal+(sal*0.20)
#                 print("El nuevo salario es:",sal)
#             else:
#                 print("No digito ninguna categoria!")

#---------------------------------IF con Ope "AND"----------------------------------

# licen=input("Digite 'si' o 'no', si usted tiene licencia: ")
# licen_lower=licen.lower()
# ingle=input("Digite 'si' o 'no', si usted sabe ingles: ")
# ingle_lower=ingle.lower()

# if (licen=="si" and ingle== "si"):
#     print("Usted esta contratado")
# else:
#     print("Usted no cumple los requisitos")

#---------------------------------IF con Ope "OR"----------------------------------

# licen=input("Digite 'si' o 'no', si usted tiene licencia: ")
# licen_lower=licen.lower()
# ingle=input("Digite 'si' o 'no', si usted sabe ingles: ")
# ingle_lower=ingle.lower()

# if (licen=="si" or ingle== "si"):
#     print("Usted esta contratado")
# else:
#     print("Usted no cumple los requisitos")

#---------------------------------IF con Ope "OR" y "AND"----------------------------------

# licen=input("Digite 'si' o 'no', si usted tiene licencia: ")
# #licen_lower=licen.lower()
# ingle=input("Digite 'si' o 'no', si usted sabe ingles: ")
# #ingle_lower=ingle.lower()

# if (licen=="si" or licen=="Si" or licen== "SI" or licen=="sI") and (ingle=="si" or ingle=="Si" or ingle=="sI" or ingle=="SI"):
#     print("Usted esta contratado")
# else:
#     print("Usted no cumple los requisitos")

#---------------------------------IF con Ope "NOT"----------------------------------

# num=int(input("Digite un numero: "))
# if num >10:
#     print("el numero es de dos digitos")
# else:
#     print("el numero es de un digito")
    
