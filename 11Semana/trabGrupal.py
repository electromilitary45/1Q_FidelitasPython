pdeseados=[]
cdeseadas=[]
numprductos=int(input("Introduce el numero de productos que deseas comprar: "))

for i in range(numprductos):
    noms = input("Nombre de producto:")
    cantNomb=int(input("Cantidad a comprar: "))
    pdeseados.append(noms)
    cdeseadas.append(cantNomb)     
    
for j in range(numprductos):
    print(pdeseados[j],":",cdeseadas[j])

