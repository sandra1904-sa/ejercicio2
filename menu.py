def mostrar_menu():
    print("\n📌 Menú de Operaciones")
    print("1. Sumar")
    print("5. Multiplicar")
    print("11. Salir")

def suma(a, b):
    return a + b
def multiplicacion(a, b):
    return a * b
while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {suma(num1, num2)}")  
    elif opcion == "5":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == "11":
        print("Saliendo del programa...")
        break
    else:
        print("⚠️ Opción no válida. Inténtelo de nuevo.")
