def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error. No se puede dividir entre 0"

print(division(5,0))