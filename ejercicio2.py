def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Insertar datos")
    print("2. Modificar datos")
    print("3. Eliminar datos")
    print("4. Salir")

def mostrar_datos(persona):
    if not persona:
        print("No hay datos disponibles.")
        return
    print("\nDatos actuales de la persona:")
    for clave, valores in persona.items():
        if valores:
            print(f"{clave.capitalize()}: {', '.join(valores)}")
        else:
            print(f"{clave.capitalize()}: No hay datos")

def insertar(persona):
    print("Insertar datos:")
    persona['habilidades'] = input("Ingresa habilidades (separadas por coma): ").split(',')
    persona['intereses'] = input("Ingresa intereses (separados por coma): ").split(',')
    persona['documentos'] = input("Ingresa documentos (separados por coma): ").split(',')
    # Limpieza de espacios en blanco
    persona['habilidades'] = [h.strip() for h in persona['habilidades'] if h.strip()]
    persona['intereses'] = [i.strip() for i in persona['intereses'] if i.strip()]
    persona['documentos'] = [d.strip() for d in persona['documentos'] if d.strip()]
    print("Datos insertados correctamente.")

def modificar(persona):
    if not persona:
        print("No hay datos para modificar. Inserta primero.")
        return
    mostrar_datos(persona)
    campo = input("¿Qué campo quieres modificar? (habilidades/intereses/documentos): ").lower()
    if campo in persona:
        print(f"Datos actuales de {campo}: {', '.join(persona[campo]) if persona[campo] else 'No hay datos'}")
        print("Opciones:")
        print("1. Modificar toda la lista")
        print("2. Agregar un nuevo dato")
        print("3. Eliminar un dato específico")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            nuevos_datos = input(f"Ingresa nuevos valores para {campo} (separados por coma): ").split(',')
            persona[campo] = [x.strip() for x in nuevos_datos if x.strip()]
            print(f"{campo.capitalize()} modificados.")
        elif opcion == '2':
            nuevo = input(f"Ingresa el nuevo dato para agregar a {campo}: ").strip()
            if nuevo:
                if nuevo not in persona[campo]:
                    persona[campo].append(nuevo)
                    print(f"'{nuevo}' agregado a {campo}.")
                else:
                    print(f"'{nuevo}' ya existe en {campo}.")
            else:
                print("Dato vacío no agregado.")
        elif opcion == '3':
            if not persona[campo]:
                print(f"No hay datos para eliminar en {campo}.")
                return
            eliminar_dato = input(f"Ingresa el dato que quieres eliminar de {campo}: ").strip()
            if eliminar_dato in persona[campo]:
                persona[campo].remove(eliminar_dato)
                print(f"'{eliminar_dato}' eliminado de {campo}.")
            else:
                print(f"'{eliminar_dato}' no se encontró en {campo}.")
        else:
            print("Opción no válida.")
    else:
        print("Campo no válido.")

def eliminar(persona):
    if not persona:
        print("No hay datos para eliminar.")
        return
    mostrar_datos(persona)
    campo = input("¿Qué campo quieres eliminar? (habilidades/intereses/documentos/todo): ").lower()
    if campo == 'todo':
        persona.clear()
        print("Todos los datos eliminados.")
    elif campo in persona:
        persona[campo] = []
        print(f"{campo.capitalize()} eliminados.")
    else:
        print("Campo no válido.")

def main():
    persona = {}
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            insertar(persona)
        elif opcion == '2':
            modificar(persona)
        elif opcion == '3':
            eliminar(persona)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
        mostrar_datos(persona)

if __name__ == "__main__":
    main()
