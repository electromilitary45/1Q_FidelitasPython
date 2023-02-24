#-------------------------------------------------ejercio1---------DEREK LEIVA----------------------------------------------------------------------
# cursos=[] #creamos una lista vacia
# for i in range(3):
#     cursos.append([0]*5) #agregamos una lista de 5 elementos a la lista vacia

# def ingresoNotas():
#     for i in range(3):
#         for j in range(5):
#             cursos[i][j]=int(input(f"Ingrese nota del estudiante{j+1} del curso{i+1}:")) #ingresamos las notas

# def promNotas():
#     suma=0
#     for i in range(3): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             suma+=cursos[i][j] #sumamos las notas
            
#     prom=suma/15 #calculamos el promedio
#     print("El promedio de las notas de los estudiantes es: ",prom) #imprimimos el promedio

# def calcNotas():
#     suma1=0
#     suma2=0
#     suma3=0
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             suma1+=cursos[0][j] #sumamos las notas
            
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             suma2+=cursos[1][j] #sumamos las notas
    
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             suma3+=cursos[2][j] #sumamos las notas
            
#     prom1=suma1/5 #calculamos el promedio1
#     prom2=suma2/5 #calculamos el promedio2
#     prom3=suma3/5 #calculamos el promedio3
    
#     print("El promedio del curso 1 es: ",prom1) #imprimimos la suma1
#     print("El promedio del curso 2 es: ",prom2) #imprimimos la suma2
#     print("El promedio del curso 3 es: ",prom3) #imprimimos la suma3

# def promAprov():
#     suma1=0
#     suma2=0
#     suma3=0
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             if cursos[0][j]>=70:
#                 suma1=suma1+1 
                
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             if cursos[1][j]>=70:
#                 suma2=suma2+1
                
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             if cursos[2][j]>=70:
#                 suma3=suma3+1 
#     porc1=(suma1/100)*100 
#     porc2=(suma2/100)*100
#     porc3=(suma3/100)*100
#     print("El porcentaje de aprobados del curso 1 es: ",porc1)
#     print("El porcentaje de aprobados del curso 2 es: ",porc2)
#     print("El porcentaje de aprobados del curso 3 es: ",porc3)

# def notaMayorMenor():
#     mayor1=0
#     mayor2=0
#     mayor3=0
#     menor1=100
#     menor2=100
#     menor3=100
    
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             if cursos[0][j]>mayor1:
#                 mayor1=cursos[0][j]
#             if cursos[0][j]<menor1:
#                 menor1=cursos[0][j]
                
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             if cursos[1][j]>mayor2:
#                 mayor2=cursos[1][j]
#             if cursos[1][j]<menor2:
#                 menor2=cursos[1][j]
                
#     for i in range(1): #recorremos la lista de 3 cursos
#         for j in range(5): #recorremos la lista
#             if cursos[2][j]>mayor3:
#                 mayor3=cursos[2][j]
#             if cursos[2][j]<menor3:
#                 menor3=cursos[2][j]
#     print("La nota mayor del primer cursos es",mayor1,"y la peor nota es",menor1)
#     print("La nota mayor del segundo cursos es",mayor2,"y la peor nota es",menor2)
#     print("La nota mayor del tercer cursos es",mayor3,"y la peor nota es",menor3)

# #-------------programa principal----------------

# # print("Las notas de los estudiantes en los 3 cursos son:")
# # #arreglo para imrpimir matriz
# # for i in range(3):
# #     for j in range(5):
# #         print(f"{cursos[i][j]:>3}",end="")
# #     print()

# ingresoNotas()
# promNotas()
# calcNotas()
# promAprov()
# notaMayorMenor()




#-----------------------------------------------------Ejercicio 2-------------------------------------------------------------------------------------------
# servicios=[] #lista para almacenar los servicios

# for i in range(4):
#     servicios.append([0]*5) #agregamos 4 filas y 4 columnas

# def verMatriz():
#     for i in range(4):
#         for j in range(5):
#             print(f"{servicios[i][j]:>3}",end="")
#         print()
        
# verMatriz()
# def ingresarServicios(): #ingresar datos matriz
#     for i in range(4):
#         for j in range(5):
#             servicio=int(input(f"Ingrese el servicio {i+1}-{j+1}: "))
#             if(servicio>=61):
#                 servicio=int(input("El servicio no puede ser mayor o igual a 60, ingrese nuevamente: "))
#                 servicios[i][j]=servicio
#             else:
#                 servicios[i][j]=servicio

# def promDiario():
#     suma1=0
#     suma2=0
#     suma3=0
#     suma4=0
    
#     for i in range(1):
#         for j in range(5):
#             suma1=suma1+servicios[0][j]
#     for i in range(1):
#         for j in range(5):
#             suma2=suma2+servicios[1][j]
#     for i in range(1):
#         for j in range(5):
#             suma3=suma3+servicios[2][j]
#     for i in range(1):
#         for j in range(5):
#             suma4=suma4+servicios[3][j]
    
#     prom1=suma1/5
#     prom2=suma2/5
#     prom3=suma3/5
#     prom4=suma4/5
#     print("El promedio del dia es: ",prom1)
#     print("El promedio del dia es: ",prom2)
#     print("El promedio del dia es: ",prom3)
#     print("El promedio del dia es: ",prom4)
    
# def promGeneral():
#     suma=0
#     for i in range(4):
#         for j in range(5):
#             suma=suma+servicios[i][j]
#     suma=suma+servicios[i][j]
#     prom=suma/20
#     print("El promedio general es: ",prom)

# def mejorServicio():
#     suma1=0
#     suma2=0
#     suma3=0
#     suma4=0
    
#     for i in range(1):
#         for j in range(5):
#             suma1=suma1+servicios[0][j]
#     for i in range(1):
#         for j in range(5):
#             suma2=suma2+servicios[1][j]
#     for i in range(1):
#         for j in range(5):
#             suma3=suma3+servicios[2][j]
#     for i in range(1):
#         for j in range(5):
#             suma4=suma4+servicios[3][j]
    
#     #comparar cual suma es mayor
#     if(suma1>suma2 and suma1>suma3 and suma1>suma4):
#         print("El servicio mejor es el 1")
#     elif(suma1<suma2 and suma1<suma3 and suma1<suma4):
#         print("El servicio mejor es el 4")
#     elif(suma2>suma1 and suma2>suma3 and suma2>suma4):
#         print("El servicio mejor es el 2")
#     else:
#         print("El servicio mejor es el 3")
#     #comparar cual suma es menor
#     if(suma1<suma2 and suma1<suma3 and suma1<suma4):
#         print("El servicio peor es el 1")
#     elif(suma1>suma2 and suma1>suma3 and suma1>suma4):
#         print("El servicio peor es el 4")
#     elif(suma2<suma1 and suma2<suma3 and suma2<suma4):
#         print("El servicio peor es el 2")
#     else:
#         print("El servicio peor es el 3")
    
# #promedio principal
# ingresarServicios()
# verMatriz()
# print("-----------")
# promDiario()
# print("-----------")
# promGeneral()
# print("-----------")
# mejorServicio()

#-----------------------------------------------------Ejercicio 3----------------------------------------------------------------------------------------------

# jugadores=[] #lista para almacenar los salarios jugadores
# for i in range(25):
#     jugadores.append(0) #agregamos 25 filas

# def verArray():
#     for i in range(len(jugadores)):
#         print(f"{jugadores[i]:>3}",end=" ||")
#     print()

# def agregarSalarios():
#     for i in range(len(jugadores)):
#         salario=int(input(f"Ingrese el salario del jugador {i+1}: "))
#         jugadores[i]=salario
        
# def deposito():
#     #cuantos billetes de 1000 ocupa para sacar
#     for i in range(len(jugadores)):
#         #billetes 20000
#         d20000=jugadores[i]//20000
#         q20000=jugadores[i]%20000
#         #billetes 10000
#         d10000=q20000//10000
#         q10000=q20000%10000
#         #billetes 5000
#         d5000=q10000//5000
#         q5000=q10000%5000
#         #billetes 2000
#         d2000=q5000//2000
#         q2000=q5000%2000
#         #billetes 1000
#         d1000=q2000//1000
#         q1000=q2000%1000
#         #monedas 500
#         d500=q1000//500
#         q500=q1000%500
#         #monedas 100
#         d100=q500//100
#         q100=q500%100
#         #monedas 50
#         d50=q100//50
#         q50=q100%50
#         #modedas 25
#         d25=q50//25
#         q25=q50%25
#         #modedas 10
#         d10=q25//10
#         q10=q25%10
#         #modedas 5
#         d5=q10//5
#         q5=q10%5
        
#         print(f"Jugador {i+1} tiene: {jugadores[i]}")
#         print(f"{d20000} billetes de 20000")
#         print(f"{d10000} billetes de 10000")
#         print(f"{d5000} billetes de 5000")
#         print(f"{d2000} billetes de 2000")
#         print(f"{d1000} billetes de 1000")
#         print(f"{d500} monedas de 500")
#         print(f"{d100} monedas de 100")
#         print(f"{d50} monedas de 50")
#         print(f"{d25} monedas de 25")
#         print(f"{d10} monedas de 10")
#         print(f"{d5} monedas de 5")
#         print(f"{q5} saldo sobrante")
#         print("--------------------------------")

# #------------programa principal---------
# agregarSalarios()
# verArray()
# deposito()

#-----------------------------------------------------Ejercicio 4---------------------------------------------------------------------------------------------
# import os

# #configurar archivo
# file=open("LISTA.txt","a")

# def agregarPersona():
#     file=open("LISTA.txt","r")
#     lista=file.readlines()
#     if len(lista)>9:
#         print("No se pueden agregar mas personas, ya que el abastecedor esta lleno")
#     else:
#         file=open("LISTA.txt","a")
#         nom=input("Ingrese el nombre: ")
#         file.write(nom+"\n")
#         file.close()

# def eliminarPersona():
#     file=open("LISTA.txt","r")
#     lista=file.read()
#     if lista=="":
#         print("No hay ninguna persona en la lista")
#     else:
#         file=open("LISTA.txt","r")
#         lista=file.readlines()
#         if len(lista)==1:
#             print("No se puede eliminar la persona, ya que solo hay una persona en la lista")
#         else:
#             file=open("LISTA.txt","r")
#             lista=file.readlines()
#             print("Personas en la lista: ")
#             for i in range(len(lista)):
#                 print(f"{i+1}-{lista[i]}")
#             num=int(input("Ingrese el numero de la persona que desea eliminar: "))
#             if num>len(lista):
#                 print("El numero ingresado no existe")
#             else:
#                 file=open("LISTA.txt","r")
#                 lista=file.readlines()
#                 file=open("LISTA.txt","w")
#                 for i in range(len(lista)):
#                     if i!=num-1:
#                         file.write(lista[i])
#                 file.close()
# #---------------------------------------------------Aplciacion principal------------------------------------
# num=""
# while num!=0:
#     num=int(input("1. Agregar persona  2.Eliminar personna  0.Salir: "))
#     if num==1:
#         agregarPersona()   
#     elif num==2:
#         eliminarPersona()
#     elif num==0:
#         print("Gracias por usar el sistema")

