saldo = 5
contador = 0
continuar = "si"
while continuar == "si" and saldo >= 1.50:
    print("Elige una opcion del menú")
    print("1. Papas fritas (Bs. 1.50)")
    print("2. Chocolate (Bs. 2.00)")
    print("3. Refresco (Bs. 2.50)")
    print("0. Salir")
    opcion = input("Elige el numero del produto que deseas comprar: ").strip()
    compra = False
    if opcion ==  "1":
        if saldo >= 1.50:
            saldo = saldo - 1.50
            contador = contador + 1
            print("Compraste Papas")
            compra = True
        else:
            print("Saldo insuficiente para comprar Papas.")
    elif opcion == "2":
        if saldo >= 2.00:
            saldo = saldo - 2.00
            contador = contador + 1
            print("Compraste Chocolate")
            compra = True
        else:
            print("Saldo insuficiente para comprar chocolate.")
    elif opcion == "3":
        if saldo >= 2.50:
            saldo = saldo - 2.50
            contador = contador + 1
            print("Compraste un Refresco.")
            compra = True
        else:
            print("Saldo insuficiente para comprar Refresco.")
    elif opcion == "0":
        continuar = "n"
        print("Decidiste salir.")
    else:
        print("Opcion no valida. Intente de nuevo.")
    if opcion != "0" and saldo >= 1.50:
        respuesta = input("¿Deseas realizar otra compra? (s/n): ").strip().lower()
        if respuesta == "n" or respuesta == "no":
            continuar = "n"
    if saldo < 1.50 and opcion != "0":
        print("Tu saldo restante no es suficiente para comprar mas productos.")
print("Cantidad de productos comprados: ",contador)
print("Tu cambio devuelto es: Bs. ",saldo)