#--------Funciones


def suma():
    print("Digite numeros a sumar")
    a=int(input("PRIMER NUMERO: "))
    b=int(input("SEGUNDO NUMERO: "))
    suma=a+b
    print("La suma es,",suma)
    
def resta():
    print("Digite numeros a restar")
    a=int(input("PRIMER NUMERO: "))
    b=int(input("SEGUNDO NUMERO: "))
    resta=a-b
    print("La resta es,",resta)

def multi():
    print("Digite numeros a multi")
    a=int(input("PRIMER NUMERO: "))
    b=int(input("SEGUNDO NUMERO: "))
    multi=a*b
    print("La multi es,",multi)

def divi():
    print("Digite numeros a dividir")
    a=int(input("PRIMER NUMERO: "))
    b=int(input("SEGUNDO NUMERO: "))
    divi=a/b
    print("La divi es",divi)

#-------Programa principal

print("Bienvenido a la calculadora")
op=int(input("Dgite que operacion realizar: 1=Suma, 2=Resta, 3=Division, 4=Multiplicacion: "))
if op==1:
    suma()
elif op==2:
    resta()
elif op== 4:
    multi()
else:
    divi() 

