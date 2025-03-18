def mostrar_menu():
    print("\n📌 Menú de Operaciones")
    print("1. Sumar")
    print("2. Restar")
    print("5. Salir")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {suma(num1, num2)}")

    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {resta(num1, num2)}")


    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("⚠️ Opción no válida. Inténtelo de nuevo.")
