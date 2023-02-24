#-----Como hacer Areglos----
# edad=[23,54,12,21,81,14,16,20,21,10]

#-----print arrelgo----------------------------
# print(edad[5],edad[6])
# print(edad)

#-----print calculados--------------------------
# print(edad[1]-edad[2])
# print(edad[2]-3)
# print(edad[1]/edad[9]) 
# print(edad[edad[2]-3]) #resta de indices

#---cambio de variable--------------------------
# print(edad[1])
# edad[1]=100 # cambio de variable
# print(edad[1])

#agregar numeros a arreglo----------------------
# print(edad)
# edad.append(100) #se agrega
# print(edad)

#elimiar dato de arreglo------------------------
# print(edad)
# edad.pop() #aqui elimina al ultimo de la fila
# print(edad)

#eliminar dato especifico-----------------------
# print(edad)
# edad.pop(2) #elimnar el dato especifico
# print(edad)

#elimnar contenido de un indice arreglo-------------

# print(edad)
# edad.remove(81)
# edad.remove(21)
# print(edad)


#---DIFERENTES FORMAS PARA IMPRIMIR UN ARREGLO CON CICLOS-----------

#caso1:---------------------------

# for x in range(10): #imprime de la posicion 0 hasta la posicion 10
#     print(edad[x]) #imprime la posiciones x
#     multi=x*edad[x] #prueba
#     print(multi)

#caso2:----------------------------

# for x in range(len(edad)):
#     print(edad[x])

# print(len(edad),"cantidad de numeros")

#caso3:-----------------------------
# for x in edad:
#     print(x)

#-----Declarar un array desde 0

# salario=[]

#-----------------------proceso de llenar arreglo-------------

# for x in range(10):
#     sal=int(input("Digite un salario: "))
#     salario.append(sal) #agregar
#     print(salario) #para ver en vivo lo cambios

#toltal de los salario-----
# tsal=0
# for j in range(10): #recorer arreglo lleno y acumular datos
#     tsal=tsal+salario[j]
# print(tsal)
#promedio de salario----
# prom=tsal/10
# print("El promedio de los Salarios es",prom)

#salario mayor------
# mayor=0
# for x in range(10):
#     if salario[x]>0:
#         mayor=salario[x]
# print(mayor)

# for x in range(10):
#     print("Salario #",x,"$:",salario[x])



