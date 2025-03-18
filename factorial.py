def factorial(a): 
    b = a
    res = 1
    if a==0:
        return 1
    else: 
        for i in range(b):
            res = res*a
            a = a-1  
    return res

#num1 = int(input("Ingrese el un número: "))
#print(factorial(num1))
