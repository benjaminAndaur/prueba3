ventaPasajes =[]

def comprarPasajes():
    cantidadPasajes=int(input("Ingrese las cantidad de pasajes a comprar: "))
    while cantidadPasajes == "":
        print("\nERROR debe ingresar una opcion")
    while True:
        print("""El precio de los asientos son los siguientes:
          (1) Asiento común, $60.000 pesos
          (2) Espacio adicional para piernas, $80.000 pesos
          (3) No reclina, $50.000 pesos""" )
        opc=int(input("Ingrese opcion:"))
        if opc ==1:
            cantidadPasajes = cantidadPasajes  * 60000
            break
        elif opc==2:
            cantidadPasajes= cantidadPasajes* 80000
            break
        elif opc ==3:
            cantidadPasajes= cantidadPasajes*50000
            break
        else: 
            print("opcion no valida")
            opc=int(input("Ingrese opcion:"))
    rut=int(input("Ingrese rut: "))
    print("La operacin se a reaizado correctamente")

        

def ubicacionesDispo():
    pass

def listarPasajeros():
    pass

def buscarPasajero():
    pass

def reasignarAsiento():
    pass

def mostrarGanancias():
    pass