#------------Ejercicio#1---------
def Ejer1():
    acumApr=0
    acumApla=0
    acumRep=0
    for i in range(10):
        num = int(input("Digite la nota: "))
        if(num>=70):
            acumApr=acumApr+1
        elif(num>=60):
            acumApla=acumApla+1
        else:
            acumRep=acumRep+1

    print("La cantidad de estudiantes aprobados es"
        ,acumApr,"\nLa cantidad de estudiantes aplazados es"
        ,acumApla,"\nLa cantidad de estudiantes reprobados es",acumRep)

#-------------Ejercicio#2---------
def Ejer2():
    AcumCla=0
    acumAct=0
    for i in range(10):
        num = int(input("Digite el año de su vehiculo: "))
        if(num<1990):
            AcumCla=AcumCla+1
        else:
            acumAct=acumAct+1

    print("Usted tiene",acumAct,"autos actuales y",AcumCla,"autos clasicos.")

#-----------Ejercicio#3---------
def Ejer3():
    acumSalMenor=0
    acumSalMayor=0
    acumSalarios=0
    tipoCam=int(input("Digite el tipo de Cambio del dolar:"))

    for i in range(6):
        sal=int(input("Digite los salarios en colones de los empleados: "))
        #cambio de salario a dolares
        sal=sal//tipoCam
        if(sal<1000):
            #acum de salarios menores a 1000
            acumSalMenor=acumSalMenor+1
            #acum de salarios colones
            acumSalarios=acumSalarios+sal
            #problema
            cantEmp=1000*acumSalMenor
            rest=cantEmp-acumSalarios
        else:
            acumSalMayor=acumSalMayor+1

    print("Los que ganan menos de $1000 necesitan"
        ,rest,"dolares para poder ganar todos $1000\nY los que ganan mas de $1000 son",acumSalMayor)

#--------------Ejercicio#4----------------

# num=0
# while num!=4:
#     num=int(input("Seleccione un Ejercicio digitando  ('1','2','3' o '4' para salir): "))
#     if(num==1):
#         Ejer1()
#     elif(num==2):
#         Ejer2()
#     elif(num==3):
#         Ejer3()
#     else:
#         print("CHAO")
    
#--------------Ejercicio#5----------------

# num1=""
# num2=""
# while num1==num2:
#     num1=int(input("Digite un num1: "))
#     num2=int(input("Digite un num2: "))
    
#     if(num1==num2):
#         print("Son iguales")
#     elif(num1<num2):
#         print("El numero 2 es mayor")
#     else:
#         print("El numero1 es mayor")

#--------------Ejercicio#6----------------
acumMa10=0
acumMe0=0
acumMa1_10=0
for i in range (5):
    num= int(input("Digite numero a calcular: "))
    if(num<0):
        acumMe0=acumMe0+1
    elif(num>=1 and num<=10):
        acumMa1_10=acumMa1_10+1
    else:
        acumMa10=acumMa10+1
    
print("Hay",acumMe0,"numeros menores a '0'",
        "\nHay",acumMa1_10,"numero mayores a '1' y menores a '10'",
        "\nHay,",acumMa10,"numeros mayores a '10'")