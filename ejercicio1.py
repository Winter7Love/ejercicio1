def insertar(lista):
    try:
        n = int(input("¿Cuántos números quieres insertar? "))
        for _ in range(n):
            num = int(input("Ingresa un número entero: "))
            lista.append(num)
        print("Datos insertados.")
        mostrar_lista(lista)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

def modificar(lista):
    try:
        if not lista:
            print("La lista está vacía.")
            return
        print("Lista actual:", lista)
        pos = int(input("Ingresa la posición del número a modificar (empezando desde 0): "))
        if pos < 0 or pos >= len(lista):
            print("Posición inválida.")
            return
        nuevo_valor = int(input("Ingresa el nuevo número: "))
        lista[pos] = nuevo_valor
        print("Número modificado.")
        mostrar_lista(lista)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

def eliminar(lista):
    try:
        if not lista:
            print("La lista está vacía.")
            return
        print("Lista actual:", lista)
        valor = int(input("Ingresa el número que quieres eliminar: "))
        if valor in lista:
            lista.remove(valor)
            print(f"El número {valor} fue eliminado.")
            mostrar_lista(lista)
        else:
            print("El número no está en la lista.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

def buscar(lista):
    try:
        if not lista:
            print("La lista está vacía.")
            return
        valor = int(input("Ingresa el número que quieres buscar: "))
        if valor in lista:
            print(f"El número {valor} se encuentra en la lista.")
        else:
            print(f"El número {valor} no está en la lista.")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")

def mostrar_menor(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        print("El número menor es:", min(lista))

def mostrar_mayor(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        print("El número mayor es:", max(lista))

def mostrar_lista(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        print("Lista actual:", lista)

def mostrar_menu():
    opciones = (
        "1. Insertar",
        "2. Modificar",
        "3. Eliminar",
        "4. Buscar",
        "5. Mostrar menor",
        "6. Mostrar mayor",
        "7. Mostrar lista completa",
        "8. Salir"
    )
    print("\nMenú de Opciones:")
    for opcion in opciones:
        print(opcion)

def main():
    lista = []
    acciones = {
        '1': insertar,
        '2': modificar,
        '3': eliminar,
        '4': buscar,
        '5': mostrar_menor,
        '6': mostrar_mayor,
        '7': mostrar_lista
    }

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '8':
            print("Saliendo del programa...")
            break
        elif opcion in acciones:
            acciones[opcion](lista)
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
