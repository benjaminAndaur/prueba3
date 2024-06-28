ventaPasajes =[]
pasajeros=[]
cantidadPasaje=[]
total =[]

def comprarPasajes():
    nombre=input("Ingrese su nombre: ").lower()
    cantidadPasajes=int(input("Ingrese las cantidad de pasajes a comprar: "))
    while cantidadPasajes == "":
        print("\nERROR debe ingresar una opcion:")
        cantidadPasajes=int(input("Ingrese las cantidad de pasajes a comprar: "))
    while True:
        print("""El precio de los asientos son los siguientes:
          (1) Asiento común, $60.000 pesos
          (2) Espacio adicional para piernas, $80.000 pesos
          (3) No reclina, $50.000 pesos""" )
        opc=int(input("Ingrese opcion: "))
        if opc ==1:
            valorPasaje = cantidadPasajes  * 60000
            break
        elif opc==2:
            valorPasaje= cantidadPasajes* 80000
            break
        elif opc ==3:
            valorPasaje= cantidadPasajes*50000
            break
        else: 
            print("opcion no valida")
            opc=int(input("Ingrese opcion: "))
    rut=int(input("Ingrese rut: "))
    print("La operacion se a realizado correctamente")

    pasajeros.append({
        'nombre':nombre,
        'rut':rut,
        'cantidadPasajes':cantidadPasajes,
        'total': valorPasaje
    })
    cantidadPasaje.append({
        'cantidad':cantidadPasajes
    })
    total.append({
        'total':valorPasaje
    })

        

def ubicacionesDispo():
    pass

def listarPasajeros():
    for pasajero in pasajeros:
        print(pasajero)

def buscarPasajero():
    rutPasajero=int(input("Ingresa el rut del pasajero a buscar: "))
    if  rutPasajero == pasajeros[0]:
        print("rl pasajero se encuentra en el vuelo")
    else:
        print("El pasaero o se encuentra en el vuelo")
        

def reasignarAsiento():
    pass

def mostrarGanancias():
    print(f"""\n\nTipo de asiento \t\t\tCantidad \t\t\t Total
(1) Asiento común, $60.000 pesos   \t\t{cantidadPasaje}      {total}
(2) Espacio adicional para piernas, $80.000 pesos\t\t
(3) No reclina, $50.000 pesos                        \t\t\n\n        """)
pasajeros=[]

while True:
    print("Sistema de control de venta")
    print("[1] Comprar pasajes")
    print("[2] Mostrar ubicaciones disponibles")
    print("[3] Ver listado de pasajeros")
    print("[4] Buscar pasajero")
    print("[5] Reasignar asiento")
    print("[6] Mostrar ganancias totales")
    print("[7] sair")
    opcion = int(input("Ingrese una opcion: "))
    
    if opcion== 1:
        comprarPasajes()
    elif opcion== 2:
        ubicacionesDispo()
    elif opcion== 3:
        listarPasajeros()
    elif opcion== 4:
        buscarPasajero()
    elif opcion== 5:
        reasignarAsiento()
    elif opcion== 6:
        mostrarGanancias()
    elif opcion== 7:
        break
    else:
        print("Opcion no valida, intente nuevamente")