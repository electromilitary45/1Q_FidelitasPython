#--------Funciones


def suma(x,y):
    suma=x+y
    print("La suma es,",suma)
def resta(x,y):
    resta=x-y
    print("La resta es,",resta)

def multi(x,y):
    multi=x*y
    print("La multi es,",multi)

def divi(x,y):
    divi=x/y
    print("La divi es",divi)

#-------Programa principal

print("Bienvenido a la calculadora")
op=int(input("Dgite que operacion realizar: 1=Suma, 2=Resta, 3=Division, 4=Multiplicacion: "))
a=int(input("PRIMER NUMERO: "))
b=int(input("SEGUNDO NUMERO: "))
if op==1:
    suma(a,b)
elif op==2:
    resta(a,b)
elif op== 4:
    multi(a,b)
elif op==3:
    divi(a,b) 

