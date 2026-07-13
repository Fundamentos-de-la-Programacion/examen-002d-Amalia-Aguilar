juegos = {
"G001": ["Eclipse Runner", "PC", "accion", "T", True, "NovaStudio"],
"G002": ["Puzzle Atlas", "Switch", "puzzle", "E", False, "BrightWorks"],
"G003": ["Sky Legends", "PS5", "aventura", "T", True, "OrionGames"],
"G004": ["Racing Pulse", "PC", "carreras", "E", True, "VelocityLab"],
"G005": ["Mystic Farm", "Switch", "simulacion", "E", False, "GreenSeed"],
"G006": ["Shadow Tactics", "Xbox", "estrategia", "M", False, "IronGate"],
          #Juego     plataforma   genero    clasificacion   multijugador  editor
}

inventario = {
"G001": [9990, 7],
"G002": [19990, 0],
"G003": [42990, 3],
"G004": [14990, 5],
"G005": [17990, 9],
"G006": [39990, 2],
     # precio stock
}



def menu():
    print("""
    ========== MENÚ PRINCIPAL ==========
1. Stock por plataforma
2. Búsqueda de juegos por rango de precio
3. Actualizar precio de juego
4. Agregar juego
5. Eliminar juego
6. Salir
=====================================""")
    
def arreglar_texto(texto):
    texto_corregido = texto.lower().strip()
    return texto_corregido
    

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Error, eliga una opcion del 1 al 6")
        except ValueError:
            print("Debe seleccionar una opción válida")
        break


def controlador_menu(dicc_juegos, dicc_inventario):
    while True:
        menu()
        opcion_elegida = leer_opcion()
        try:
            if opcion_elegida == 1:
                # Stock por plataforma
                while True:
                    stock_consultar = input("Ingrese plataforma a consultar: ")
                    stock_consultar = arreglar_texto(stock_consultar)
                    if stock_consultar in dicc_juegos:
                        print("Juego encontrado")
                    break

                stock_plataforma(dicc_juegos, dicc_inventario, stock_consultar)
                

            elif opcion_elegida == 2:
                # Búsqueda de juegos por rango de precio
                while True:
                    try:
                        precio_minimo = int(input("Ingrese precio mínimo: "))
                        precio_maximo = int(input("Ingrese precio máximo: "))
                        break

                    except ValueError:
                        print("Debe ingresar valores enteros")

                busqueda_precio(dicc_juegos, dicc_inventario, precio_minimo, precio_maximo)

                
            elif opcion_elegida == 3:
                # Actualizar precio juego
                while True:
                    try:
                        codigo_para_actualizar = input("Ingrese código del juego: "). upper() #para que g00X sea G00X
                        precio_a_actualizar = int(input("Ingrese nuevo precio: "))
                        if codigo_para_actualizar == False:
                            print("El código no existe")
                        else:
                            print("Precio actualizado")
                            otro_precio = input("¿Desea actualizar otro precio (s/n): ").lower()
                            if otro_precio == "s":
                                codigo_para_actualizar = input("Ingrese código del juego: "). upper() #para que g00X sea G00X
                                precio_a_actualizar = int(input("Ingrese nuevo precio: "))
                            else:
                                break

                        break
                    except ValueError:
                        print("Debe ingresar valores enteros")

                buscar_codigo(dicc_juegos, dicc_inventario, codigo)



                
            elif opcion_elegida == 4:
                # Agregar juego
                while True:
                    try:
                        nuevo_codigo = input("Ingrese código del juego: ").upper().split()
                        nuevo_titulo = input("Ingrese título: ")
                        nueva_plataforma = input("Ingrese plataforma: ")
                        nuevo_genero = input("Ingrese género: ")
                        nueva_clasificacion = input("Ingrese clasificación: ").upper()
                        nuevo_multiplayer = input("¿Es multiplayer? (s/n): ").lower()
                        nuevo_editor = input("Ingrese editor: ")
                        nuevo_precio = int(input("Ingrese precio: "))
                        nuevo_stock = int(input("Ingrese stock: "))

                        print("Juego agregado")
                    except ValueError:
                        print("Error de precio o stock")
                    break

                agregar_juego(dicc_juegos, dicc_inventario, codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock)


            elif opcion_elegida == 5:
                # Eliminar juego
                codigo_a_eliminar = input("Ingrese el codigo del juego que desea eliminar: ").upper()

                if eliminar_juego(dicc_juegos, dicc_inventario, codigo):
                    print("Juego eliminado")
                

            elif opcion_elegida == 6:
                # Salir
                print("Programa finalizado.")
                break

        except ValueError:
            print("Error")

# Opcion 1 — Stock por plataforma
def stock_plataforma(dicc_juegos, dicc_inventario, plataforma):
    for codigo, datos in dicc_inventario.items():
        print(f"el total de stock disponible es: {datos[1]}: {codigo}")
    else:
        print("No se ha encontrado esa plataforma")

# Opcion 2 — Búsqueda de juegos por rango de precio
def busqueda_precio(dicc_juegos, dicc_inventario, p_min, p_max):
    if p_min > p_max and p_min < 0 or p_max < 0:
        print("El precio minimo no puede ser mayor al maximo y los precios tienen que ser mayor a 0")
        return
    encontrado = False
    for codigo, datos in dicc_inventario.items():
        precio_juego = datos[0]
        if p_min <= precio_juego <= p_max:
            nombre_juego = dicc_juegos[codigo][0]
            print(f"Juego: {nombre_juego}, precio: {precio_juego}")
            encontrado = True

    if not encontrado:
        print("No se encontró el juego")

    busqueda_precio(dicc_juegos, dicc_inventario, p_min, p_max)


# Opcion 3 — Actualizar precio de juego
def buscar_codigo(dicc_juegos, dicc_inventario, codigo):
    for c in dicc_inventario:
        if c == codigo:
            return True
        
        return False
         
    buscar_codigo(dicc_juegos, dicc_inventario, codigo)

# Opcion 4 — Agregar juego
def agregar_juego(dicc_juegos, dicc_inventario, codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock):
    codigo = False
    for c in dicc_inventario:
        if c in dicc_inventario or c == codigo in dicc_juegos:
            print("El código ya existe")
        else:
            print("Juego agregado")
            codigo = True

        if nueva_clasificacion == "s":
            return True
        else:
             return False
        
    agregar_juego(dicc_juegos, dicc_inventario, codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock)
        
# Opcion 5 — Eliminar juego
def eliminar_juego(dicc_juegos, dicc_inventario, codigo):
    
    if codigo in dicc_juegos or codigo in dicc_inventario:
        del dicc_juegos[codigo]
        del dicc_inventario[codigo]
    else:
        print("No existe el codigo")
        return False


controlador_menu(juegos, inventario)