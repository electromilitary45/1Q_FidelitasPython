#------------------------PARTE Explacion CICLOS------------------

# n1=int(input("n1: "))
# n2=int(input("n2: "))
# n3=int(input("n3: "))
# n4=int(input("n4: "))
# n5=int(input("n5: "))
# n6=int(input("n6: "))
# n7=int(input("n7: "))
# n8=int(input("n8: "))
# n9=int(input("n9: "))
# n10=int(input("n10: "))

# prom=(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)/10
# print(prom)



#---------------------Utilizando FOR---------------------------------

# for cont in range(10):
#     print("Vuelta numero",cont)

# print("Termine")
#------------------------------
#variable acum
acum=0
num=0
for cont in range(10):
    num=int(input("Digite el numero: "))
    acum=acum+num
    prom=acum/10
print("El promedio es: ",prom)

#-----Mejora---

# acum=0
# num=0

# n=int(input("Digite la cantidad de numeros que quiere calcular: "))
# for cont in range(n):
#     num=int(input("Digite el numero: "))
#     acum=acum+num
#     prom=acum/n
# print("EL promedio es",prom)


#----WHILE-----
# num=int(input("Digite un numero: "))
# Tnum=0
# vuelta=-1

# while num!=0:
#     num=int(input("Digite el numero: "))
#     Tnum=Tnum+num
#     vuelta=vuelta+1


# prom=Tnum/vuelta
# print(prom)

#----------user

# usuario=""
# passw=""
# while usuario !="admin" or passw !="123":
#     usuario=input("Usuario")
#     passw=input("Passw")
#     if usuario=="admin" and passw =="123":
#         print("Bienvenido")
#     else:
#         print("Error")


