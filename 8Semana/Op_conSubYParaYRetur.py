#--------Funciones


def suma(x,y):
    suma=x+y
    return suma
def resta(x,y):
    resta=x-y
    return resta

def multi(x,y):
    multi=x*y
    return multi

def divi(x,y):
    divi=x/y
    return divi

#-------Programa principal

print("Bienvenido a la calculadora")
op=int(input("Dgite que operacion realizar: 1=Suma, 2=Resta, 3=Division, 4=Multiplicacion: "))
a=int(input("PRIMER NUMERO: "))
b=int(input("SEGUNDO NUMERO: "))
if op==1:
    print("La suma es",suma(a,b))
elif op==2:
    print("La resta es",resta(a,b))
elif op== 4:
    print("La multi es",multi(a,b))
else:
    print("La divi es",divi(a,b)) 
    
# op=0
# while op!=4:
#     op=int(input("Dgite que operacion realizar: 1=Suma, 2=Resta, 3=Division, 4=Multiplicacion: "))    
#     a=int(input("PRIMER NUMERO: "))
#     b=int(input("SEGUNDO NUMERO: "))
#     if op==1:
#         print("La suma es",suma(a,b))
#     elif op==2:
#         print("La resta es",resta(a,b))
#     elif op== 4:
#         print("La multi es",multi(a,b))
#     else:
#         print("La divi es",divi(a,b)) 


