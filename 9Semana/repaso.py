# nombres=["juan","pedro","maria","jose"]
# nums=[0,10,2,35,4,5,6,7,8,9,0,20,30,20]

#----impresiones
# print(nombres[1]) #imprime un nombre
# print(nums[9]-2) #a la posicion 9 se le restan 2

#Asignaciones
# nums[1]=nums[9]-2
# print(nums)

#-----agregar nuevos numeros
# print(nums)
# nums.append(111)
# print(nums)

#-----eliminar numeros

# print(nums)
# nums.pop() #elimina el ultimo elemento
# print(nums)

# print(nums)
# nums.pop(4) #elimina el elemento en la posicion 4
# print(nums)

#------eliminar posciones

# print(nums)
# nums.remove(20) #elimina la posicion donde tenga el valor 20 el primero que encuentre
# print(nums)

#-----print con ciclo

# for i in range(len(nums)):   #len(nums) es la longitud de la lista
#     print(nums[i])

#-----print con ciclo diractamente con array

# for i in nums:
#     print(i)

#----agregar datos a un array vacio

# edades=[]
# cEdades=int(input("Cuantas edades quiere registrar: "))
# for i in range(cEdades):
#     edad=int(input("Ingrese edad: "))
#     edades.append(edad)
# for x in edades:
#     print(x)

#-----------------------Ejercio1----------------------------
array=[]
num=int(input("Ingrese un numero: "))

for i in range(num):
    array.append(num)

print(array)

#-----------------------Ejercio2----------------------------

for i in range(len(array)):
    array[i]=10+i

print(array)