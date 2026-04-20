from Clases.Auto import *
from Clases.Moto import *
from Clases.Colectivo import *
from Clases.AutoHibrido import *
from Clases.ClaseAbstracta import *
from Clases.AutoElectrico import *
from Clases.Furgon import *



# ===================== Persistencia =====================
# Listas globales
autos, motos, colectivos, AutHibr, AutoElec, furgones = [], [], [], [], [], []


def guardar_vehiculos():
    # Autos
    with open("Datos/autos.txt", "w") as f:
        for v in autos:
            f.write(f"{v.marca},{v.modelo},{v._Vehiculo__patente},{v.puertas}\n")

    # Motos
    with open("Datos/motos.txt", "w") as f:
        for v in motos:
            f.write(f"{v.marca},{v.modelo},{v._Vehiculo__patente},{v.cilindrada}\n")

    # Colectivos
    with open("Datos/colectivos.txt", "w") as f:
        for v in colectivos:
            f.write(f"{v.marca},{v.modelo},{v._Vehiculo__patente},{v.capacidad}\n")

    # Autos híbridos
    with open("Datos/autohibridos.txt", "w") as f:
        for v in AutHibr:
            f.write(f"{v.marca},{v.modelo},{v._Vehiculo__patente},{v.puertas},{v.bateria}\n")

    # Autos eléctricos 100%
    with open("Datos/autoelectricos.txt", "w") as f:
        for v in AutoElec:
            f.write(f"{v.marca},{v.modelo},{v.patente},{v.bateria},{v.sistema_autopilot}\n")

    # Furgones (Herencia híbrida Colectivo + Auto)
    with open("Datos/furgones.txt", "w") as f:
        for v in furgones:
            f.write(f"{v.marca},{v.modelo},{v._Vehiculo__patente},{v.capacidad},{v.puertas}\n")


def cargar_vehiculos():
    global autos, motos, colectivos, AutHibr, AutoElec, furgones
    autos, motos, colectivos, AutHibr, AutoElec, furgones = [], [], [], [], [], []

    # --- AUTOS ---
    try:
        with open("Datos/autos.txt", "r") as f:
            for line in f:
                marca, modelo, patente, puertas = line.strip().split(",")
                autos.append(Auto(marca, modelo, patente, int(puertas)))
    except FileNotFoundError:
        pass

    # --- MOTOS ---
    try:
        with open("Datos/motos.txt", "r") as f:
            for line in f:
                marca, modelo, patente, cilindrada = line.strip().split(",")
                motos.append(Moto(marca, modelo, patente, cilindrada))
    except FileNotFoundError:
        pass

    # --- COLECTIVOS ---
    try:
        with open("Datos/colectivos.txt", "r") as f:
            for line in f:
                marca, modelo, patente, asientos = line.strip().split(",")
                colectivos.append(Colectivo(marca, modelo, patente, int(asientos)))
    except FileNotFoundError:
        pass

    # --- AUTOS HÍBRIDOS ---
    try:
        with open("Datos/autohibridos.txt", "r") as f:
            for line in f:
                marca, modelo, patente, puertas, bateria = line.strip().split(",")
                AutHibr.append(AutoHibrido(marca, modelo, patente, int(puertas), float(bateria)))
    except FileNotFoundError:
        pass

    # --- AUTOS ELÉCTRICOS ---
    try:
        with open("Datos/autoelectricos.txt", "r") as f:
            for line in f:
                marca, modelo, patente, bateria, autopilot = line.strip().split(",")
                AutoElec.append(AutoElectrico(marca, modelo, patente, float(bateria), autopilot))
    except FileNotFoundError:
        pass

    # --- FURGONES ---
    try:
        with open("Datos/furgones.txt", "r") as f:
            for line in f:
                marca, modelo, patente, asientos, puertas = line.strip().split(",")
                furgones.append(Furgon(marca, modelo, patente, int(asientos), int(puertas)))
    except FileNotFoundError:
        pass


    
def mostrar_vehiculo(tipo):
    if tipo == "auto":    
        for ve in autos:
            ve.tipo()

    elif tipo == "moto":
        for ve in motos:
            ve.tipo()

    elif tipo == "colectivo":        
        for ve in colectivos:
            ve.tipo()

    elif tipo == "autohibrido":
        for ve in AutHibr:
            ve.tipo()
    elif tipo == "autoelectrico":
        for ve in AutoElec:
            ve.info()
    elif tipo == "furgon":
        for ve in furgones:
            ve.tipo()
    else:
        print("Opción inválida.")

def Patente_mostrar(tipo):

    # ===================== AUTO =====================
    if tipo == "auto":
        if not autos:
            print("No hay autos cargados.")
            return
        for ve in autos:
            print(ve.mostrarPatente)

    # ===================== MOTO =====================
    elif tipo == "moto":
        if not motos:
            print("No hay motos cargadas.")
            return
        for ve in motos:
            print(ve.mostrarPatente)

    # ===================== COLECTIVO =====================
    elif tipo == "colectivo":
        if not colectivos:
            print("No hay colectivos cargados.")
            return
        for ve in colectivos:
            print(ve.mostrarPatente)

    # ===================== AUTO HÍBRIDO =====================
    elif tipo == "autohibrido":
        if not AutHibr:
            print("No hay autos híbridos cargados.")
            return
        for ve in AutHibr:
            print(ve.mostrarPatente)

    # ===================== AUTO ELÉCTRICO =====================
    elif tipo == "autoelectrico":
        if not AutoElec:
            print("No hay autos eléctricos cargados.")
            return
        for ve in AutoElec:
            print(ve.mospaten())

    # ===================== FURGÓN =====================
    elif tipo == "furgon":
        if not furgones:
            print("No hay furgones cargados.")
            return
        for ve in furgones:
            print(ve.mostrarPatente)

    else:
        print("Opción inválida.")


def VehiculosArrancarTodos():
    hay_vehiculos = False
    
    print("-----------AUTOS----------------")
    for ve in autos:
        ve.arrancar()
        hay_vehiculos = True
    
    print("-----------MOTOS----------------")

    for ve in motos:
        ve.arrancar()
        hay_vehiculos = True
        
    print("-----------COLECTIVOS----------------")

    for ve in colectivos:
        ve.arrancar()
        hay_vehiculos = True

    print("-----------AUTOSHIBRIDOS----------------")

    for ve in AutHibr:
        ve.arrancar()
        hay_vehiculos = True
    
    print("-----------AUTOSELECTRICOS----------------")

    for ve in AutoElec:
        ve.arrancar()
        hay_vehiculos = True
    
    print("-----------FURGONES----------------")

    for ve in furgones:
        ve.arrancar()
        hay_vehiculos = True

    if not hay_vehiculos:
        print("No hay vehículos cargados.")



def crear_vehiculo(tipo):
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    patente = input ("Patente: ")

    if tipo == "auto":
        puertas = int(input("Puertas: "))
        obj = Auto(marca, modelo,patente, puertas)
        autos.append(obj)

    elif tipo == "moto":
        cilindrada = input("Cilindrada (cc): ")
        obj = Moto(marca, modelo,patente, cilindrada)
        motos.append(obj)

    elif tipo == "colectivo":
        capacidad = int(input("Capacidad de pasajeros: "))
        obj = Colectivo(marca, modelo,patente, capacidad)
        colectivos.append(obj)

    elif tipo == "autohibrido":
        puertas = int(input("Puertas: "))
        bateria = float(input("Capacidad de batería (kWh): "))
        obj = AutoHibrido(marca, modelo,patente, puertas, bateria)
        AutHibr.append(obj)

    elif tipo == "autoelectrico":
        sistema_autopilot = input("sistema_autopilot: ")
        bateria = float(input("Capacidad de batería (kWh): "))
        obj = AutoElectrico(marca, modelo, patente, bateria, sistema_autopilot)
        AutoElec.append(obj) 

    elif tipo == "furgon":
        puertas = int(input("Puertas: "))
        capacidad = int(input("Capacidad de pasajeros: "))
        obj = Furgon(marca, modelo, patente, capacidad, puertas)
        furgones.append(obj)

    
    guardar_vehiculos()   # <<<<<<<<<<<<<< AGREGAR ESTO
    print("Vehículo guardado correctamente.\n")


def eliminar_vehiculo(tipo):

    # ===================== AUTO =====================
    if tipo == "auto":
        if not autos:
            print("No hay autos cargados.")
            return

        print("\nLista de Autos:")
        for i, a in enumerate(autos, start=1):
            print(f"{i}. {a.marca} {a.modelo} - Patente: {a.patente}")

        try:
            indice = int(input("\nElegí el número del Auto a eliminar: ")) - 1
            if indice < 0 or indice >= len(autos):
                print("Índice inválido.")
                return
        except ValueError:
            print("Tenés que ingresar un número.")
            return

        eliminado = autos.pop(indice)
        guardar_vehiculos()
        print(f"\nAuto eliminado correctamente: {eliminado.marca} {eliminado.modelo}")

    # ===================== MOTO =====================
    elif tipo == "moto":
        if not motos:
            print("No hay motos cargadas.")
            return

        print("\nLista de Motos:")
        for i, m in enumerate(motos, start=1):
            print(f"{i}. {m.marca} {m.modelo} - Patente: {m.patente}")

        indice = int(input("\nElegí el número de la Moto a eliminar: ")) - 1
        eliminado = motos.pop(indice)
        guardar_vehiculos()
        print(f"\nMoto eliminada correctamente: {eliminado.marca} {eliminado.modelo}")

    # ===================== COLECTIVO =====================
    elif tipo == "colectivo":
        if not colectivos:
            print("No hay colectivos cargados.")
            return

        print("\nLista de Colectivos:")
        for i, c in enumerate(colectivos, start=1):
            print(f"{i}. {c.marca} {c.modelo} - Patente: {c.patente}")

        eliminado = colectivos.pop(int(input("\nElegí el número: ")) - 1)
        guardar_vehiculos()
        print(f"\nColectivo eliminado correctamente: {eliminado.marca} {eliminado.modelo}")

    # ===================== AUTO HÍBRIDO =====================
    elif tipo == "autohibrido":
        if not AutHibr:
            print("No hay autos híbridos cargados.")
            return

        print("\nLista de Autos Híbridos:")
        for i, a in enumerate(AutHibr, start=1):
            print(f"{i}. {a.marca} {a.modelo} - Patente: {a.patente}")

        eliminado = AutHibr.pop(int(input("\nElegí el número: ")) - 1)
        guardar_vehiculos()
        print(f"\nAuto híbrido eliminado correctamente: {eliminado.marca} {eliminado.modelo}")

    # ===================== AUTO ELÉCTRICO =====================
    elif tipo == "autoelectrico":
        if not AutoElec:
            print("No hay autos eléctricos cargados.")
            return

        print("\nLista de Autos Eléctricos:")
        for i, e in enumerate(AutoElec, start=1):
            print(f"{i}. {e.marca} {e.modelo} - Patente: {e.patente}")

        eliminado = AutoElec.pop(int(input("\nElegí el número: ")) - 1)
        guardar_vehiculos()
        print(f"\nAuto eléctrico eliminado correctamente: {eliminado.marca} {eliminado.modelo}")

    # ===================== FURGÓN =====================
    elif tipo == "furgon":
        if not furgones:
            print("No hay furgones cargados.")
            return

        print("\nLista de Furgones:")
        for i, f in enumerate(furgones, start=1):
            print(f"{i}. {f.marca} {f.modelo} - Patente: {f.patente}")

        eliminado = furgones.pop(int(input("\nElegí el número: ")) - 1)
        guardar_vehiculos()
        print(f"\nFurgón eliminado correctamente: {eliminado.marca} {eliminado.modelo}")

    else:
        print("Tipo de vehículo no válido.")



def modificar_vehiculo(tipo):

    # ===================== AUTO =====================
    if tipo == "auto":
        if not autos:
            print("No hay autos cargados.")
            return

        print("\nLista de Autos:")
        for i, auto in enumerate(autos, start=1):
            print(f"{i}. {auto.marca} {auto.modelo} - Patente: {auto.patente} - Puertas: {auto.puertas}")

        try:
            indice = int(input("\nElegí el número del Auto a modificar: ")) - 1
            if indice < 0 or indice >= len(autos):
                print("Índice inválido.")
                return
        except ValueError:
            print("Tenés que ingresar un número.")
            return

        auto = autos[indice]

        print("\n¿Qué querés modificar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Patente")
        print("4. Puertas")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            auto.marca = input("Nueva marca: ")
        elif opcion == "2":
            auto.modelo = input("Nuevo modelo: ")
        elif opcion == "3":
            auto.patente = input("Nueva patente: ").upper()
        elif opcion == "4":
            auto.puertas = int(input("Cantidad de puertas: "))
        else:
            print("Opción inválida.")
            return

        guardar_vehiculos()
        print("\nAuto modificado correctamente.")
        auto.tipo()

    # ===================== MOTO =====================
    elif tipo == "moto":
        if not motos:
            print("No hay motos cargadas.")
            return

        print("\nLista de Motos:")
        for i, moto in enumerate(motos, start=1):
            print(f"{i}. {moto.marca} {moto.modelo} - Patente: {moto.patente} - Cilindrada: {moto.cilindrada}")

        indice = int(input("\nElegí el número de la Moto: ")) - 1
        moto = motos[indice]

        print("\n¿Qué querés modificar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Patente")
        print("4. Cilindrada")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            moto.marca = input("Nueva marca: ")
        elif opcion == "2":
            moto.modelo = input("Nuevo modelo: ")
        elif opcion == "3":
            moto.patente = input("Nueva patente: ").upper()
        elif opcion == "4":
            moto.cilindrada = input("Nueva cilindrada (cc): ")
        else:
            print("Opción inválida.")
            return

        guardar_vehiculos()
        print("\nMoto modificada correctamente.")
        moto.tipo()

    # ===================== COLECTIVO =====================
    elif tipo == "colectivo":
        if not colectivos:
            print("No hay colectivos cargados.")
            return

        print("\nLista de Colectivos:")
        for i, c in enumerate(colectivos, start=1):
            print(f"{i}. {c.marca} {c.modelo} - Patente: {c.patente} - Capacidad: {c.capacidad}")

        c = colectivos[int(input("\nElegí el número: ")) - 1]

        print("\n¿Qué querés modificar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Patente")
        print("4. Capacidad")

        op = input("Opción: ")

        if op == "1":
            c.marca = input("Nueva marca: ")
        elif op == "2":
            c.modelo = input("Nuevo modelo: ")
        elif op == "3":
            c.patente = input("Nueva patente: ").upper()
        elif op == "4":
            c.capacidad = int(input("Nueva capacidad: "))
        else:
            print("Opción inválida.")
            return

        guardar_vehiculos()
        print("\nColectivo modificado correctamente.")
        c.tipo()

    # ===================== AUTO HÍBRIDO =====================
    elif tipo == "autohibrido":
        if not AutHibr:
            print("No hay autos híbridos cargados.")
            return

        print("\nLista de Autos Híbridos:")
        for i, a in enumerate(AutHibr, start=1):
            print(f"{i}. {a.marca} {a.modelo} - Patente: {a.patente} - Puertas: {a.puertas} - Batería: {a.bateria}")

        a = AutHibr[int(input("\nElegí el número: ")) - 1]

        print("\n¿Qué querés modificar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Patente")
        print("4. Puertas")
        print("5. Batería")

        op = input("Opción: ")

        if op == "1":
            a.marca = input("Nueva marca: ")
        elif op == "2":
            a.modelo = input("Nuevo modelo: ")
        elif op == "3":
            a.patente = input("Nueva patente: ").upper()
        elif op == "4":
            a.puertas = int(input("Puertas: "))
        elif op == "5":
            a.bateria = float(input("Batería (kWh): "))
        else:
            print("Opción inválida.")
            return

        guardar_vehiculos()
        print("\nAuto híbrido modificado correctamente.")
        a.tipo()

    # ===================== AUTO ELÉCTRICO =====================
    elif tipo == "autoelectrico":
        if not AutoElec:
            print("No hay autos eléctricos cargados.")
            return

        print("\nLista de Autos Eléctricos:")
        for i, e in enumerate(AutoElec, start=1):
            print(f"{i}. {e.marca} {e.modelo} - Patente: {e.patente} - Batería: {e.bateria} - Autopilot: {e.sistema_autopilot}")

        e = AutoElec[int(input("\nElegí el número: ")) - 1]

        print("\n¿Qué querés modificar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Patente")
        print("4. Batería")
        print("5. Autopilot")

        op = input("Opción: ")

        if op == "1":
            e.marca = input("Nueva marca: ")
        elif op == "2":
            e.modelo = input("Nuevo modelo: ")
        elif op == "3":
            e.patente = input("Nueva patente: ").upper()
        elif op == "4":
            e.bateria = float(input("Batería (kWh): "))
        elif op == "5":
            e.sistema_autopilot = input("Autopilot (sí/no): ")
        else:
            print("Opción inválida.")
            return

        guardar_vehiculos()
        print("\nAuto eléctrico modificado correctamente.")
        e.info()

    # ===================== FURGÓN =====================
    elif tipo == "furgon":
        if not furgones:
            print("No hay furgones cargados.")
            return

        print("\nLista de Furgones:")
        for i, f in enumerate(furgones, start=1):
            print(f"{i}. {f.marca} {f.modelo} - Patente: {f.patente} - Capacidad: {f.capacidad} - Puertas: {f.puertas}")

        f = furgones[int(input("\nElegí el número: ")) - 1]

        print("\n¿Qué querés modificar?")
        print("1. Marca")
        print("2. Modelo")
        print("3. Patente")
        print("4. Capacidad")
        print("5. Puertas")

        op = input("Opción: ")

        if op == "1":
            f.marca = input("Nueva marca: ")
        elif op == "2":
            f.modelo = input("Nuevo modelo: ")
        elif op == "3":
            f.patente = input("Nueva patente: ").upper()
        elif op == "4":
            f.capacidad = int(input("Capacidad: "))
        elif op == "5":
            f.puertas = int(input("Puertas: "))
        else:
            print("Opción inválida.")
            return

        guardar_vehiculos()
        print("\nFurgón modificado correctamente.")
        f.tipo()

    else:
        print("Tipo de vehículo no válido.")

