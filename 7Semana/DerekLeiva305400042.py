print("Bievenido al programa de Video Mania")

num=""
while num!=5:
    print("*******MENU******************************\n",
        "*****1=Incluir Cliente*******\n",
        "*****2=Alquilar pelicula*****\n",
        "*****3=Estadistica***********\n",
        "*****4=Promociones***********\n",
        "*****5=Salir*****************\n",
        "************************************")
    num=int(input("Introduzca el numero del Modulo usar: "))
    
    if num ==1:
        print("********INCLUSION DE CLIENTES******")
        ced=int(input("Digite su # de Cedula: "))
        nom=input("Digite su nombre: ")
        edad=int(input("Digite su edad: "))
        while edad<18:
            edad=int(input("Digite su edad: "))
        
        dir=input("Digite su direccion: ")
        estCivil=input("Digite su estado civil: ")
        correo=input("Digite su correo: ")
        
        print("Afiliacion Realizada con exito\n",
                "Bievenido",nom,"cedula:",ced,"..Disfruta!")
    #fin Incuir Cliente
    if num==2:
        print("********AlQUILER Y FACTURACION DE PELICULAS******")
        ced=int(input("Digite su cedula: "))
        cantPeli=int(input("Digite la cantidad de Peliculas que desea llevar: "))
        precio=int(input("Precio de pelicula: "))
        
        if cantPeli >=7:
            des=(cantPeli*precio)*0.20
            preFin=(cantPeli*precio)-des
        elif cantPeli==5:
            des=(cantPeli*precio)*0.15
            preFin=(cantPeli*precio)-des
        elif cantPeli<5:
            des=(cantPeli*precio)*0.05
            preFin=(cantPeli*precio)-des
        
        print("Usted",ced,"alquila",cantPeli,"por un precio de",precio,"\nel monto a descuentar es de",
                des,"y el monto final a pagar es de",preFin,
                "\nUsted tiene 6 dias para devolver la pelicula")        
    #fin ALQUILER
    if num==3:
        
        print("INFORME DE PELICULAS RENTADAS")
        num=int(input("Peliculas a calcular: "))
        bat=0
        sup=0
        flash=0
        for i in range(num):
            pel=int(input("Tipo de pelicula (1=batman, 2=Superman, 3=Flash): "))
            if pel==1:
                bat=bat+1
            elif pel==2:
                sup=sup+1
            elif pel==3:
                flash=flash+1
        print("En total se alquilaron:",bat,"Peliculas de Batman",sup,"Peliculas de Superman",flash,"Peliculas de flash")        
    #fin informe
    if num==4:
        print("ENCUESTA DE LA SEMANA")
        
        rom=0
        accion=0
        infan=0
        drama=0
        
        for i in range(10):
            enc=int(input("Tipo de pelicula que mas le gusta (1=Romantica, 2=Accion, 3=Infantiles, 4=Drama): "))
            if enc==1:
                rom=rom+1
            elif enc==2:
                accion=accion+1
            elif enc==3:
                infan=infan+1
            elif enc==4:
                drama=drama+1
            
        porcRom=rom*10
        porcAccion=accion*10
        porcInfan=infan*10
        porcDrama=drama*10
            
        print("------------------\nCantidad de votos:\n",
            "VOTOS ROMANTICAS:",rom,"equivalente a",porcRom,"%\n",
            "VOTOS ACCION:",accion,"equivalente a",porcAccion,"%\n",
            "VOTOS INFANTILES:",infan,"equivalente a",porcInfan,"%\n",
            "VOTOS DRAMA:",drama,"equivalente a",porcDrama,"%")
    #fin Encuesta