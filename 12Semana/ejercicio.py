#----------imports----------
import os

#-----------------Declaracion de Arreglos--------------

#----Arraysnombres---
trabajadores=[]
for i in range(4):
        trabajadores.append([0]*4) #agregamos una lista de 4 elementos a la lista vacia

#---------------------FUNCIONES--------------------
def ansTrabajadores(): #esta funcion es para agregar los datos de los trabajadores
    for i in range(4):
        for j in range(4):
            trabajadores[i][j]=int(input(f"Ingrese los años de laborados del trabajador {i+1} Departamento {j+1}: "))

def verArray(): #esta funcion es para ver el arreglo
    for i in range(len(trabajadores)):
        print(trabajadores[i])
        
def promedioGeneral(): #esta funcion es para sacar el promedio general de todos los trabajadores
    suma=0
    for i in range(4):
        for j in range(4):
            suma+=trabajadores[i][j]
    prom=suma/16
    print(f"El promedio de los trabajadores del departamento 1 es: {prom}")
        

def edadPromedio(): #esta funcion es para sacar la edad promedio de los trabajadores
    for i in range(len(trabajadores)):
        suma=0
        for j in range(len(trabajadores[i])):
            suma+=trabajadores[i][j]
        print(f"La edad promedio de los trabajajadores del departamento {i+1} es: {suma/4}")

    # for i in range(4):
    #     ans=int(input("Ingrese los años de laborados del trabajador: "))

def promPensionados(): #esta funcion es para sacar el promedio de los pensionados
    suma=0
    for i in range(len(trabajadores)):
        for j in range(len(trabajadores[i])):
            if trabajadores[i][j]>=33:
                suma+=1
    
    prom=(suma/100)*100
    print("El porcentaje de pensionados es: ",prom)
    
def menormayor(): #esta funcion es para sacar las edades menores y mayores 
    mayor1=0
    mayor2=0
    mayor3=0
    menor1=100
    menor2=100
    menor3=100
    
    for i in range(1):
        for j in range(4):
            if trabajadores[i][j]>mayor1:
                mayor1=trabajadores[i][j]
            if trabajadores[i][j]<menor1:
                menor1=trabajadores[i][j]
                
    for i in range(1):
        for j in range(4):
            if trabajadores[i+1][j]>mayor2:
                mayor2=trabajadores[i+1][j]
            if trabajadores[i+1][j]<menor2:
                menor2=trabajadores[i+1][j]
    
    for i in range(1):
        for j in range(4):
            if trabajadores[i+2][j]>mayor3:
                mayor3=trabajadores[i+2][j]
            if trabajadores[i+2][j]<menor3:
                menor3=trabajadores[i+2][j]
    
    print("La edad mayor del Departamento 1 es",mayor1,"y la menor es",menor1)
    print("La edad mayor del Departamento 2 es",mayor2,"y la menor es",menor2)
    print("La edad mayor del Departamento 3 es",mayor3,"y la menor es",menor3)
#-----------------APLICATIVO-----------------------

usuario=""
passw=""
print("Bienvenido, user: admin, passw: 123") 
while usuario !="admin" or passw !="123":
    usuario=input("Usuario: ")
    passw=input("Passw: ")
    if usuario=="admin" and passw =="123":
        print("Bienvenido al ejericio final del curso <3",
            "\nCalculo de Trabajadores")
        
        ansTrabajadores()
        verArray()
        print("----")
        promedioGeneral()
        print("----")
        edadPromedio()
        print("----")
        promPensionados()
        print("----")
        menormayor()
    else:
        print("Usuario o contraseña incorrecta")




