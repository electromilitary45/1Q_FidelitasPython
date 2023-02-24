#EXAMEN || DEREK SEBASTIAN LEIVA VILLALOBOS || 3005400042 || 22/04/2022

def Censo():
    tipoContratacion=[]
    edadPersonas=[]

    for i in range(10):
        tipoContratacion.append(input(f"Ingrese el tipo de contratacion 'persona #{i+1}' 'Propiedad' o Interno': "))
        edadPersonas.append(int(input(f"Ingrese la edad de la persona #{i+1}: "))) 

    print(tipoContratacion)        
    #Tipo de contractacion =1 Propiedad
    #Tipo de contractacion =2 Interno
    
    sumaTPro=0
    sumaTInter=0
    
    #----Edades propiedad--
    sumaMayorEdadPropi=0
    sumaMenorEdadPropi=0
    #-----edades interno---
    sumaMayorEdadInter=0
    sumaMenorEdadInter=0
    edadMP=0
    for i in range(len(tipoContratacion)):
        #---Calculo personas propiedad---
        if tipoContratacion[i]=="Propiedad":
            sumaTPro=sumaTPro+1
        #---Calculo personas interno---
        if tipoContratacion[i]=="Interno":
            sumaTInter=sumaTInter+1
        
        #---Calculo edades propiedad---
        if edadPersonas[i]>=18 and tipoContratacion[i]=="Propiedad":
            sumaMayorEdadPropi=sumaMayorEdadPropi+1
        else:
            sumaMenorEdadPropi=sumaMenorEdadPropi+1
        
        #---Calculo edades interno---
        if edadPersonas[i]>=18 and tipoContratacion[i]=="Interno":
            sumaMayorEdadInter=sumaMayorEdadInter+1
        else:
            sumaMenorEdadInter=sumaMenorEdadInter+1
        if tipoContratacion[i]=="Propiedad" > edadMP:
            edadMP=tipoContratacion[i]
            
    #---Calculo porcentaje propiedad e Intera---
    calcPropiedad=(sumaTPro*100)/10
    calcInterno=(sumaTInter*100)/10
    #---Calculo porcentaje edades propiedad e interno---
    calcEdadMaPropiedad=(sumaMayorEdadPropi*100)/10
    calcEdadMePropiedad=(sumaMenorEdadPropi*100)/10
    #--
    calcEdadMaInter=(sumaMayorEdadInter*100)/10
    calcEdadMeInter=(sumaMenorEdadInter*100)/10
    
    
    
    print("---------\n"+"Hay un",calcPropiedad,"% personas contratadas en propiedad y",calcInterno,"% de personas contratadas en Interna")
    print("---------\n"+"Hay un",calcEdadMaPropiedad,"% de mayores de edad contratadas en propiedad y",calcEdadMePropiedad,"% de menores de edad en propiedad")
    print("---------\n"+"Hay un",calcEdadMaInter,"% de mayores de edad contratadas en Interno y",calcEdadMeInter,"% de menores de edad en Interno")
    print("---------\n"+"La persona con mayor edad es de",edadMP,"años")

def Zonas():
    
    #declaracion de Vectores
    zonas=[]
    monto=[]
    
    for i in range(10):
        zonas.append(input(f"Ingrese la zona #{i+1} ('Norte, Sur, Este, Oeste'): "))
        monto.append(int(input(f"Ingrese el monto de la zona #{i+1}: ")))
    
    #suma de montos
    sumaN=0
    cantN=0
    #---
    sumaS=0
    cantS=0
    #----
    sumaE=0
    cantE=0
    #----
    sumaO=0
    cantO=0
    
    for i in range(10):
        
        if zonas[i]=="Norte":
            sumaN=sumaN+monto[i]
            cantN=cantN+1
        elif zonas[i]=="Sur":
            sumaS=sumaS+monto[i]
            cantS=cantS+1
        elif zonas[i]=="Este":
            sumaE=sumaE+monto[i]
            cantE=cantE+1
        elif zonas[i]=="Oeste":
            sumaO=sumaO+monto[i]
            cantO=cantO+1
    #calculo promedio de montos
    calcMN=sumaN/cantN
    calcMS=sumaS/cantS
    calcME=sumaE/cantE
    calcMO=sumaO/cantO
    #----repuestas---
    print("---------\n"+"El promedio de los montos de las zonas son:\n")
    print("Norte:",calcMN,"₡\n")
    print("Sur:",calcMS,"₡\n")
    print("Este:",calcME,"₡\n")
    print("Oeste:",calcMO,"₡\n")
    
def FrutosTropicales():
    
    def ingresoPersonas():
        nombre=input("Ingrese el nombre de la persona: ")
        file=open("PersonasIngresadas.txt","a")
        file.write(nombre+"\n")
        file.close()
        FrutosTropicales()


    def traspasoPersonas():
        file=open("PersonasIngresadas.txt","r")
        contenido=file.read()#cargar datos
        convec=contenido.split("\n")#convertir a lista
        print(convec)
        #EXAMEN || DEREK SEBASTIAN LEIVA VILLALOBOS || 3005400042 || 22/04/2022

    def cantPedro():
        file=open("PersonasIngresadas.txt","r")
        contenido=file.read() #cargar todo el contenido del archivo en una variable
        convec=contenido.split("\n") #separar el contenido en un arreglo
        
        contar=0
        for i in range(len(convec)):
            if convec[i]=="Pedro":
                contar=contar+1
        print("Existen:",contar,"personas con el nombre Pedro")
        file.close()
    
    #-----programa principal---
    print("**********************************")
    print("-----Menu Frutos Tropicales--------")
    print("----1.Ingreso de Personas-----")
    print("----2.Traspaso de nombres-----")
    print("----3.Ver cantidad de Pedros-------")
    print("----------0.Salir--------------")
    print("***************************")
    
    num=""
    while num!=0:
        num=int(input("Ingrese el numero del Programa: "))
        if num==1:
            ingresoPersonas()
            #EXAMEN || DEREK SEBASTIAN LEIVA VILLALOBOS || 3005400042 || 22/04/2022
        elif num==2:
            traspasoPersonas()
        elif num==3:
            cantPedro()
        elif num==0:
            break
    
#-----------------------programa principal----------------------
num=""
while num!=0:
    print("**********MENU*****************")
    print("*  1. Censo de personas  *")
    print("*  2. Calculo de montos Zonas  *")
    print("*  3. Frutos Tropicales  *")
    print("*  0. Salir                *")
    print("********************************\n")
    
    num=int(input("A que problema quiere ingresar: "))
    if num==1:
        Censo()
    elif num==2:
        Zonas()
    elif num==3:
        FrutosTropicales()
    elif num==0:
        print("Gracias por usar el programa")
        break

#EXAMEN || DEREK SEBASTIAN LEIVA VILLALOBOS || 3005400042 || 22/04/2022