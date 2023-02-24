from ast import Mult
from cmath import inf

#----------Ejercicio#1
def tablamulti(a):
    for i in range(1,12):
        multi=a*i
        print(a,"x",i,"=",multi)
    
#----------Ejercicio#2
def calcPeso(cant):
    pesoEntre20y30=0
    pesoEntre30y50=0
    pesomas50=0
    for i in range(cant):
        nino=int(input("Digite el peso del nino: "))
        
        if nino>=20 and nino<30:
            pesoEntre20y30=pesoEntre20y30+1
        elif nino>=30 and nino<50:
            pesoEntre30y50=pesoEntre30y50+1
        else:
            pesomas50=pesomas50+1
            
    print("pesoEntre20y30",pesoEntre20y30,
        "\nPeso entre30y50",pesoEntre30y50,
        "\nPeso mas de 50",pesomas50)
#------------Ejercicio#3
def genero():
    genF=0
    genM=0
    gen=""
    tv=-1
    while gen!="S":
        gen=input("Digite Genero F=Femenino, M=Masculino o S=Salir")
        
        if gen=="F":
            genF=genF+1
            
        if gen=="M":
            genM=genM+1
        
        tv+=1
    
    genFm=(genF*tv)/100
    genMm=(genM*tv)/100
    print("El porcentaje de hombres es",genMm,"el porcentaje de mujeres es",genFm)
#-programa

print("MENU 1=Ejercicio tabla, 2=Ejercicio peso, 3=Ejercicio genero")
menu=int(input("Digite el numero de Ejercicio: "))
if menu==1:
    print("Tabla de multiplicar")
    a=int(input("Digite el numero del cual quiera saber la tabla: "))
    tablamulti(a)
elif menu==2:
    cant=int(input("Digite el numero de niños a calcular: "))
    calcPeso(cant)
else:
    genero()

